
local set_nodes = function(pos1, pos2, item)
	local stepx=(pos1.x<=pos2.x) and 1 or -1
	local stepy=(pos1.y<=pos2.y) and 1 or -1
	local stepz=(pos1.z<=pos2.z) and 1 or -1
	for x=pos1.x,pos2.x,stepx do
		for y=pos1.y,pos2.y,stepy do
			for z=pos1.z,pos2.z,stepz do
				minetest.set_node({x=x,y=y,z=z},item)
			end
		end
	end
end

local set_nodes_rdd = function(ref, delta1, delta2, item)
	local pos1 = vector.add(ref, delta1)
	local pos2 = vector.add(ref, delta2)
	set_nodes(pos1, pos2, item)
end

local list_quiz = {
	{question="Which coordinate indicates vertical position?", answers={"x", "y", "z"}, correct=2},
	{question="What are the four parameters of the build function?", answers={"x, y, z, material", "material, x, y, z", "player, x, y, z", "length, width, height, material"}, correct=1},
	{question="What data type is (1, 2, 3)?", answers={"set", "list", "dict", "tuple"}, correct=4},
	{question="What data type is [1, 2, 3]?", answers={"set", "list", "dict", "tuple"}, correct=2},
	{question="What data type is {'a':1, 'b':2, 'c':3}?", answers={"set", "list", "dict", "tuple"}, correct=3},
	{question="What data type is {1, 2, 3}?", answers={"set", "list", "dict", "tuple"}, correct=1},
	{question="How many blocks are created: \nb='wool:red'#6_______________________\nmc.build(100,[14,15],100,b)#6_______________________", answers={"1","2","3","4"}, correct=2},
	{question="How many blocks are created: \nb='default:glass'#6_______________________\nmc.build(100,[14,15],[89,91],b)#6_______________________", answers={"1","2","3","4","6"}, correct=4},
	{question="How many blocks are created: \nb='default:glass'#6_______________________\nfor#6_#0x#6_#0in#6_#0range(0,3):#6__________________________\n#6__#0mc.build(x,14,[89,91],b)#6_______________________", answers={"4","6","9","12"}, correct=2},
	{question="What is \n \n16 + 10", answers={"1","1.6","6","26"}, correct=4},
	{question="What is \n \n16 - 10", answers={"1","1.6","6","26"}, correct=3},
	{question="What is \n \n16 // 10", answers={"1","1.6","6","26"}, correct=1},
	{question="What is \n \n16 % 10", answers={"1","1.6","6","26"}, correct=3},
	{question="What is \n \n16 / 10", answers={"1","1.6","6","26"}, correct=2},
	{question="Which python statement does not create a loop", answers={"for","while","if"}, correct=3},
	{question="What is equivalent to range(3,9,2)", answers={"(3,4,5,6,7,8,9)","(5,7)","(3,5,7,9)","(3,5,7)","()"}, correct=4},
	{question="What is equivalent to range(9,3,2)", answers={"(9,8,7,6,5,4)","(9,7,5)","(9,7,5,3)","(9)","()"}, correct=5},
}

local get_quiz = function(player_name)
	local num_quiz = builder_police.get_player_num_quiz(player_name)
	-- print("get_quiz(player_name): num_quiz")
	-- print(player_name)
	-- print(num_quiz)
	if not num_quiz or num_quiz > #list_quiz or #list_quiz == 0 then
		return nil
	end
	if num_quiz < 1 then
		num_quiz = 1
		builder_police.set_player_num_quiz(player_name, num_quiz)
	end
	local quiz = list_quiz[num_quiz]
	-- print("quiz.question")
	-- print(quiz.question)
	return quiz
end

local assign_quiz = function(player_name)
	local q = get_quiz(player_name)
	if not q then
		return
	end
	local pos_build = builder_police.pos_build(player_name) 
	if pos_build and pos_build.x and pos_build.y and pos_build.z then
		print("player_name "..player_name..", pos="..pos_build.x.." "..pos_build.y.." "..pos_build.z)
	else
		print("pos is nil")
	end
	local num = #q.answers
	local xmin = -7 - 2 * num
	local torchmz = {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})}
	local torchpz = {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=-1})}
	set_nodes_rdd(pos_build, {x=-1,y=-1,z=-5}, {x=xmin,y=-5,z=4},   {name="default:stone"})
	set_nodes_rdd(pos_build, {x=4,y=-1,z=-5}, {x=0,y=-5,z=-1},   {name="default:stone"})
	
	-- set_nodes_rdd(pos_build, {x=-1,y=-1,z=0}, {x=-1,y=0,z=0},   {name="air"}) --entrance to quiz tunnel
	set_nodes_rdd(pos_build, {x=3,y=-2,z=-1}, {x=3,y=-4,z=-4},   {name="air"}) -- quiz tunnel to the side
	set_nodes_rdd(pos_build, {x=2,y=-2,z=-4}, {x=-5,y=-4,z=-4},   {name="air"}) -- quiz tunnel to the question
	set_nodes_rdd(pos_build, {x=-6,y=-2,z=-4}, {x=xmin+1,y=-4,z=-2},   {name="air"}) -- quiz foyer to the answers - 3 blocks high to see answers
	for a=1,num do
		local x = -5 - 2 * a
		set_nodes_rdd(pos_build, {x=x,y=-3,z=-1}, {x=x,y=-4,z=2},   {name="air"}) -- quiz tunnel answer 
		irc_builder.set_sign({x=pos_build.x+x,y=pos_build.y-2,z=pos_build.z-2}, "+z", "default:sign_wall_wood", q.answers[a])
		irc_builder.set_sign({x=pos_build.x+x,y=pos_build.y-3,z=pos_build.z+2}, "+z", "default:sign_wall_wood", "please wait while\n \nwe check your answer")
	end
	for x=xmin+2,xmin+num*2,2 do
		minetest.set_node(vector.add(pos_build,{x=x,y=-4,z=-4}), torchpz)
		minetest.set_node(vector.add(pos_build,{x=x,y=-4,z= 2}), torchmz)
	end
	local sign_pos={x=pos_build.x-7,y=pos_build.y-3,z=pos_build.z-4}
	local text=player_name.."\n \n"..q.question
	irc_builder.set_sign(sign_pos, "-z", "default:sign_wall_wood", text)
	--set_nodes_rdd(pos_build, {x=xmin, y=-5, z=-3}, {x=22, y=-11, z=3}, {name="air"}) -- clear previous builds
	set_nodes_rdd(pos_build, {x=xmin, y=-5, z=-3}, {x=4, y=-11, z=3}, {name="default:stone"}) -- pool under answers
	set_nodes_rdd(pos_build, {x=5, y=-5, z=-1}, {x=22, y=-9, z=1}, {name="default:stone"}) -- tunnel out for incorrect answer
	set_nodes_rdd(pos_build, {x=xmin+1, y=-6, z=-2}, {x=3, y=-10, z=2}, {name="air"}) -- pool under answers
	set_nodes_rdd(pos_build, {x=xmin+1, y=-8, z=-2}, {x=3, y=-10, z=2}, {name="default:water_source"}) -- pool under answers
	set_nodes_rdd(pos_build, {x=4, y=-6, z=0}, {x=21, y=-7, z=0}, {name="air"})  -- tunnel out for incorrect answer
	set_nodes_rdd(pos_build, {x=21, y=-7, z=-1}, {x=22, y=-1, z=1}, {name="default:stone"}) -- shaft up for incorrect answer
	set_nodes_rdd(pos_build, {x=21, y=-7, z=0}, {x=21, y=-2, z=0}, {name="air"}) -- shaft up for incorrect answer
	set_nodes_rdd(pos_build, {x=21, y=-7, z=0}, {x=21, y=-2, z=0}, {name="default:ladder_wood", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})}) -- shaft up for incorrect answer
	set_nodes_rdd(pos_build, {x=20, y=-4, z=0}, {x=20, y=-2, z=0}, {name="air"}) -- shaft up for incorrect answer
	--set_nodes_rdd(pos_build, {x=0, y=-8, z=0}, {x=0, y=-10, z=0}, {name="default:stone"})
	for x=5,20,2 do
		minetest.set_node({x=pos_build.x+x, y=pos_build.y-7, z=pos_build.z}, torchpz)
	end
	for x=pos_build.x + xmin+2, pos_build.x + 3,2 do
		minetest.set_node({x=x, y=pos_build.y-7, z=pos_build.z+2}, torchmz)
		minetest.set_node({x=x, y=pos_build.y-7, z=pos_build.z-2}, torchpz)
	end
end

local assign_quiz_for_player = function(player)
	assign_quiz(player:get_player_name())
end

local test_quiz_for_player = function(player)
	local player_name = player:get_player_name()
	local num_quiz = builder_police.get_player_num_quiz(player_name)
	local q = get_quiz(player_name)
	if not q then
		return false
	end
	local pos_build = builder_police.pos_build(player_name)
	local p = player:getpos()

	-- first check if player in one of answer tunnels
	-- print(dump(pos_build)..dump(p))
	local answer = math.floor((pos_build.x - p.x + 0.5 - 5) / 2)
	if p and answer > 0 and answer <= #q.answers and math.abs(pos_build.y - 4 - p.y) < 1 and math.abs(pos_build.z + 2 - p.z) < 2 then
		
		p.x = math.floor(p.x + 0.5) -- convert x value to nearest integer
		
		--set_nodes_rdd(pos_build, {x=0, y=-3, z=-1}, {x=0, y=-4, z=-1}, {name="default:stone"}) -- build a wall to stop player leaving tunnel
		-- now check if in correct tunnel
		--local x = -4 - q.correct * 2
		print(player_name.." x "..p.x.." answer "..answer.." correct "..q.correct)
		if answer == q.correct then
			print("correct answer")
			minetest.chat_send_all(player_name..' has correctly answered quiz '..num_quiz)
			builder_police.set_player_num_quiz(player_name, num_quiz + 1)
			assign_quiz(player_name)
			--set_nodes_rdd(pos_build, {x=-6, y=-3, z=-2}, {x=-6-2*#q.answers, y=-4, z=-2}, {name="air"}) -- remove wall preventing user back
			player:setpos({x = pos_build.x - 7, y = pos_build.y - 4.5, z = pos_build.z - 3})
			player:set_look_horizontal(math.pi)
		else
			print("incorrect answer")
			local x = -5 - 2 * answer
			local xmin = - 7 - 2 * #q.answers 
			set_nodes_rdd(pos_build, {x=x, y=-5, z=-1}, {x=x, y=-5, z=2}, {name="air"}) -- trapdoor for incorrect answer
			minetest.chat_send_all(player_name..' has incorrectly answered quiz '..num_quiz..' so is going for a swim')
			--player:setpos({x = p.x, y = p.y - 3, z = p.z})
		end
	end
end

builder_police.assign_quiz = assign_quiz
builder_police.assign_quiz_for_player = assign_quiz_for_player
builder_police.test_quiz_for_player = test_quiz_for_player
builder_police.get_quiz = get_quiz

--builder_police.quizzes={	quiz_1_assign,}
--builder_police.quiz_tests={	quiz_1_test,}

