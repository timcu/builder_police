
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
	{
		{question="Which coordinate indicates vertical position?", answers={"x", "y", "z"}, correct=2},
		{question="What are the four parameters of the build function?", answers={"x, y, z, material", "material, x, y, z", "player, x, y, z", "length, width, height, material"}, correct=1},
	},
	{
		{question="What data type is (1, 2, 3)?", answers={"int", "list", "dict", "tuple"}, correct=4},
		{question="What data type is [1, 2, 3]?", answers={"int", "list", "dict", "tuple"}, correct=2},
	},
}

local question = function(player_name)
	local num_quiz = builder_police.get_player_quiz(player_name)
	local num_question = builder_police.get_player_question(player_name)
	if not num_quiz or num_quiz < 1 or num_quiz > #list_quiz then
		return nil
	end
	local quiz = list_quiz[num_quiz]
	if not num_question or num_question < 1 or num_question > #quiz then
		return nil
	end
	return quiz[num_question]
end

local assign_question = function(player)
	local player_name = player:get_player_name()
	local q = question(player_name)
	if not q then
		return
	end
	local pos = builder_police.pos_build(player_name) 
	local num = #q.answers
	local xmin = -5 - 2 * num
	local torchmz = {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})}
	local torchpz = {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=-1})}
	set_nodes_rdd(pos, {x=-1,y=-1,z=-5}, {x=xmin,y=-5,z=4},   {name="default:stone"})
	set_nodes_rdd(pos, {x=4,y=-1,z=-5}, {x=0,y=-5,z=-1},   {name="default:stone"})
	
	-- set_nodes_rdd(pos, {x=-1,y=-1,z=0}, {x=-1,y=0,z=0},   {name="air"}) --entrance to quiz tunnel
	set_nodes_rdd(pos, {x=3,y=-2,z=-1}, {x=3,y=-4,z=-4},   {name="air"}) -- quiz tunnel to the side
	set_nodes_rdd(pos, {x=2,y=-2,z=-4}, {x=-5,y=-4,z=-4},   {name="air"}) -- quiz tunnel to the question
	set_nodes_rdd(pos, {x=-6,y=-2,z=-4}, {x=-12,y=-4,z=-2},   {name="air"}) -- quiz foyer to the answers - 3 blocks high to see answers
	for a=1,num do
		local x = -4 - a * 2
		set_nodes_rdd(pos, {x=x,y=-3,z=-1}, {x=x,y=-4,z=2},   {name="air"}) -- quiz tunnel answer 
		irc_builder.set_sign({x=pos.x+x,y=pos.y-2,z=pos.z-2}, "+z", "default:sign_wall_wood", q.answers[a])
		irc_builder.set_sign({x=pos.x+x,y=pos.y-3,z=pos.z+1}, "-z", "default:sign_wall_wood", "please wait while\n \nwe check your answer")
	end
	for x=xmin+1,3,2 do
		minetest.set_node(vector.add(pos,{x=x,y=-4,z=-4}), torchpz)
		minetest.set_node(vector.add(pos,{x=x,y=-4,z= 1}), torchmz)
	end
	local sign_pos={x=pos.x-7,y=pos.y-3,z=pos.z-4}
	local text=player_name.."\n \n"..q.question
	irc_builder.set_sign(sign_pos, "-z", "default:sign_wall_wood", text)
end

local test_question = function(player)
	local player_name = player:get_player_name()
	local q = question(player_name)
	if not q then
		return false
	end
	local pos_build = builder_police.pos_build(player_name)
	local p = player:getpos()

	-- first check if player in one of answer tunnels
	-- print(dump(pos_build)..dump(p))
	if p and math.abs(pos_build.x - 9 - p.x) < 4 and math.abs(pos_build.y - 4 - p.y) < 1 and math.abs(pos_build.z + 1 - p.z) < 2 then
		-- build a wall to stop player leaving tunnel
		set_nodes_rdd(pos_build, {x=-6, y=-3, z=-2}, {x=-4-2*#q.answers, y=-4, z=-2}, {name="default:stone"})
		-- now check if in correct tunnel
		--local x = -4 - q.correct * 2
		local torchpz = {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=-1})}
		local answer = math.floor((pos_build.x - p.x + 0.5 - 4) / 2)
		if answer == correct then
			print("correct answer")
			return true
		else
			print("incorrect answer")
			local x = -4 - answer * 2
			set_nodes_rdd(pos_build, {x=x-1, y=-5, z=-3}, {x=22, y=-10, z=3}, "default:stone")
			set_nodes_rdd(pos_build, {x=21, y=-1, z=-1}, {x=22, y=-10, z=1}, "default:stone")
			set_nodes_rdd(pos_build, {x=x, y=-5, z=-2}, {x=0, y=-9, z=2}, "air")
			set_nodes_rdd(pos_build, {x=0, y=-5, z=0}, {x=21, y=-7, z=0}, "air")
			set_nodes_rdd(pos_build, {x=21, y=-7, z=0}, {x=21, y=-2, z=0}, "air")
			set_nodes_rdd(pos_build, {x=0, y=-7, z=0}, {x=0, y=-7, z=0}, "default:stone")
			set_nodes_rdd(pos_build, {x=x, y=-4, z=-1}, {x=x, y=-4, z=2}, "air")
			for x=0,20,2 do
				minetest.set_node({x=pos_build.x+x, y=pos.y-9, z=pos.z}, torchpx)
			end
			return false
		end
	end
end

builder_police.assign_question = assign_question
builder_police.test_question = test_question

--builder_police.quizzes={	quiz_1_assign,}
--builder_police.quiz_tests={	quiz_1_test,}

