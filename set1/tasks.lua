
local set_nodes_rdd = function(ref, delta1, delta2, item)
	local pos1 = vector.add(ref, delta1)
	local pos2 = vector.add(ref, delta2)
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

local task_1_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	set_nodes_rdd(pos, {x=-6,y=-1,z=-5}, {x=-31,y=11,z=4}, {name="default:sandstone"})
	set_nodes_rdd(pos, {x=-15,y=5,z=2},  {x=-25,y=7,z=4},  {name="default:obsidian"})
	set_nodes_rdd(pos, {x=-5,y=-1,z=-5}, {x=4,y=-1,z=4},   {name="default:stone"})
	set_nodes_rdd(pos, {x=-5,y=0,z=-5},  {x=4,y=16,z=4},   {name="air"})
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	text="Place an orange wool block at x,y,z coordinates above\n \nwool:orange"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
end

local task_1_test = function(player_name)
	local pos_build = builder_police.pos_build(player_name)
	local pos = vector.add(pos_build, {x=0,y=4,z=0})
	local pos_assess = vector.add(pos_build, {x=0,y=0,z=1})
	local node = minetest.get_node(pos)
	if node.name:find("wool:") == 1 then
		return true
	else
		local text = "Task 1 Assessment\n \nBlock is type "..node.name.." which does not start with 'wool:'"
		irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
		return false
	end
end

local task_2_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	local text="Place a glass frame around block at coordinates above. All glass blocks are to have same x value.\n \ndefault:glass"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
end

local task_2_test = function(player_name)
	local pos_build = builder_police.pos_build(player_name)
	local pos = vector.add(pos_build, {x=0,y=4,z=0})
	local pos_assess = vector.add(pos_build, {x=0,y=0,z=1})
	for y=pos.y-1,pos.y+1 do
		for z=pos.z-1,pos.z+1 do
			local node = minetest.get_node({x=pos.x,y=y,z=z})
			if z == pos.z and y == pos.y then
				if node.name:find("wool:") ~= 1 then
					local text = "Task 2 Assessment\n \nBlock in centre is type "..node.name.." which does not start with 'wool:'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false
				end
			else
				if node.name ~= "default:glass" then
					local text = "Task 2 Assessment\n \nBlock at ("..pos.x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false
				end				
			end
		end
	end
	return true
end

local task_3_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	local text="Place a glass box around block at coordinates above. .\n \ndefault:glass"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
end

local task_3_test = function(player_name)
	local pos_build = builder_police.pos_build(player_name)
	local pos = vector.add(pos_build, {x=0,y=4,z=0})
	local pos_assess = vector.add(pos_build, {x=0,y=0,z=1})
	for x=pos.x-1,pos.x+1 do
		for y=pos.y-1,pos.y+1 do
			for z=pos.z-1,pos.z+1 do
				local node = minetest.get_node({x=x,y=y,z=z})
				if x == pos.x and z == pos.z and y == pos.y then
					if node.name:find("wool:") ~= 1 then
						local text = "Task 3 Assessment\n \nBlock in centre is type '"..node.name.."' which does not start with 'wool:'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end
				else
					if node.name ~= "default:glass" then
						local text = "Task 3 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end				
				end
			end
		end
	end
	return true
end

local task_4_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	-- first clear air for tasks 6 and 7
	set_nodes_rdd(pos, {x=-10,y=12,z=-5},    {x=10,y=32,z=4},    {name="air"})
	-- assign task 4
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	local text="Climb down the ladder below this sign to see task 4"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
	set_nodes_rdd(pos, {x=-1,y=-1,z=-1},  {x=20,y=-5,z=1},    {name="default:stone"})
	set_nodes_rdd(pos, {x=1,y=-1,z=0},    {x=1,y=-4,z=0},     {name="default:ladder_wood", param2=minetest.dir_to_wallmounted({x=-1,y=0,z=0})})
	set_nodes_rdd(pos, {x=2,y=-2,z=0},    {x=19,y=-4,z=0},    {name="air"})
	for torchx=pos.x+2,pos.x+19,4 do
		minetest.set_node({x=torchx, y=pos.y-4, z=pos.z}, {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	end
	sign_pos=vector.add(pos,{x=12,y=-3,z=0})
	text="Hello "..player_name.."\n \nYour task is to create a glass tunnel with external dimensions of 5 blocks wide and 7 blocks high"
	irc_builder.set_sign(sign_pos, "+z", "default:sign_wall_wood", text)
	sign_pos=vector.add(pos,{x=16,y=-3,z=0})
	text="Centre of tunnel floor has coordinates \nx1="..(pos.x-7).." y="..(pos.y+4).." z="..pos.z.."\nand extends to\nx2="..(pos.x-30).." y="..(pos.y+4).." z="..pos.z
	irc_builder.set_sign(sign_pos, "+z", "default:sign_wall_wood", text)
	set_nodes_rdd(pos, {x=-15,y=5,z=-2}, {x=-25,y=7,z=-4}, {name="default:obsidian"})
	set_nodes_rdd(pos, {x=-16,y=6,z=-3}, {x=-24,y=6,z=-3}, {name="air"})
	minetest.set_node(vector.add(pos,{x=-17,y=6,z=-3}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=-1})})
	minetest.set_node(vector.add(pos,{x=-19,y=6,z=-3}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=-1})})
	minetest.set_node(vector.add(pos,{x=-21,y=6,z=-3}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=-1})})
	minetest.set_node(vector.add(pos,{x=-23,y=6,z=-3}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=-1})})
	sign_pos=vector.add(pos,{x=-18,y=6,z=-3})
	text="Congratulations "..player_name.."\n \nNow change the tunnel floor to stone and place a torch every 4 blocks"
	irc_builder.set_sign(sign_pos, "-z", "default:sign_wall_wood", text)
	for stair=0,4 do
		set_nodes_rdd(pos, {x=-2-stair,y=stair+1,z=-1}, {x=-2-stair,y=stair+5,z=1}, {name="air"})
		set_nodes_rdd(pos, {x=-2-stair,y=stair  ,z=-1}, {x=-2-stair,y=stair  ,z=1}, {name="stairs:stair_wood", param2=minetest.dir_to_facedir({x=-1,y=0,z=0})})		
	end
end

local task_4_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	for x=pos.x-30,pos.x-7 do
		for y=pos.y+4,pos.y+10 do
			for z=pos.z-2,pos.z+2 do
				local node=minetest.get_node({x=x,y=y,z=z})
				if y==pos.y+4 then
					-- floor should be glass or stone
					if node.name ~= "default:glass" and node.name ~= "default:stone" then
						local text = "Task 4 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end				
				elseif z==pos.z-2 or z==pos.z+2 or y==pos.y+10 then
					-- side walls and roof should be glass
					if node.name ~= "default:glass" then
						local text = "Task 4 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end
				elseif y==pos.y+5 then
					--above floor should be air or torches
					if node.name ~= "air" and node.name:find("default:torch") ~= 1 then
						local text = "Task 4 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end				
				elseif node.name ~= "air" then
					text = "Task 4 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false				
				end
			end
		end
	end
	return true
end

local task_5_assign = function(player_name)
	-- Task 5 automatically assigned when task 4 completed but repeated in case accidentally deleted
	local pos = builder_police.pos_build(player_name) 
	local sign_pos=vector.add(pos,{x=-18,y=6,z=-3})
	local text="Congratulations "..player_name.."\n \nNow change the tunnel floor to stone and place a torch every 4 blocks"
	irc_builder.set_sign(sign_pos, "-z", "default:sign_wall_wood", text)
end

local task_5_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	local torches = 0
	for x=pos.x-30,pos.x-7 do
		for y=pos.y+4,pos.y+5 do
			for z=pos.z-1,pos.z+1 do
				local node=minetest.get_node({x=x,y=y,z=z})
				if y==pos.y+4 then
					-- floor should be stone
					if node.name ~= "default:stone" then
						local text = "Task 5 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:stone'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end				
				else
					-- side walls and roof should be glass
					if node.name:find("default:torch") == 1 then
						torches = torches + 1
					elseif node.name ~= "air" then
						local text = "Task 5 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air' or 'default:torch'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end	
				end			
			end
		end
	end
	local text = "Task 5 Assessment\n \nCompleted"
	irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
	return true
end

local task_6_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	-- local pos_chest = vector.add(pos,{x=-31,y=5,z=0})
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.." Task 6\n \nChequered Square"
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)

	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	text='Construct a vertical square shape of alternating wool colours in the sky with height of 9 blocks with centre at\nx='..pos.x..' y='..(pos.y+22)..' z='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)	
end

local task_6_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	local z = pos.z
	for y=pos.y+18,pos.y+26 do
		local prev = ""
		for x=pos.x-4,pos.x+4 do
			local node=minetest.get_node({x=x,y=y,z=z})
			if node.name == prev then
				local text = "Task 6 Assessment\n \nBlocks at ("..(x-1)..", "..y..", "..z..") and ("..x..", "..y..", "..z..") are both of type '"..node.name.."' but should be different if alternating"
				irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
				return false
			end
			prev = node.name
			if node.name:find('wool') ~= 1 then
				local text = "Task 6 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be a wool type, eg 'wool:orange'"
				irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
				return false
			end	
		end
	end			
	local text = "Task 6 Assessment\n \nCompleted"
	irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
	return true
end

local task_7_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	-- local pos_chest = vector.add(pos,{x=-31,y=5,z=0})
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.." Task 7\n \nChequered Diamond"
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)

	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	text='Construct a 2D diamond shape of alternating wool colours in the sky with height of 21 blocks with centre at\nx='..pos.x..' y='..(pos.y+22)..' z='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)	
end

local task_7_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	local z = pos.z
	for j=1,21 do
		local y=pos.y+22-11+j
		local prev = ""
		local woolmin = math.abs(11-j)+1
		local woolmax = 22 - woolmin
		for i=1,21 do
			local x=pos.x-11+i
			local node=minetest.get_node({x=x,y=y,z=z})
			if i<woolmin or i> woolmax then
				if node.name ~= "air" then
					local text = "Task 7 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false
				end	
			else
				if node.name == prev then
					local text = "Task 7 Assessment\n \nBlocks at ("..(x-1)..", "..y..", "..z..") and ("..x..", "..y..", "..z..") are both of type '"..node.name.."' but should be different if alternating"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false
				end
				prev = node.name
				if node.name:find('wool') ~= 1 then
					local text = "Task 7 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be a wool type, eg 'wool:orange'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false
				end	
			end
		end
	end			
	local text = "Task 7 Assessment\n \nCompleted"
	irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
	return true
end

local task_8_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_chest = vector.add(pos,{x=-31,y=5,z=0})
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nLook in chest in your tunnel"
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)

	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	text="Task 8\n \nSloping tunnel\n \nSee book"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
	
	set_nodes_rdd(pos, {x=-31,y=4,z=-2}, {x=-33,y=10,z=2}, {name="default:meselamp"})	
	set_nodes_rdd(pos, {x=-31,y=5,z=-1}, {x=-31,y= 9,z=1}, {name="air"})	
	text='Continue glass tunnel down on a diagonal where centre of tunnel floor goes from x1='..(pos.x-31)..',y1='..(pos.y+4)..' to x2='..(pos.x-31-60)..',y2='..(pos.y+4-60)..'. z is constant z='..pos.z..'. Make sure no lava or water leak into tunnel'
	minetest.set_node(pos_chest, {name="default:chest",param2=3})
	irc_builder.add_book_to_chest(player_name, pos_chest, {title="Task 8 for "..player_name, text=text})

	set_nodes_rdd(pos, {x=-31-60-1,y=4-60  ,z=5}, {x=-31-60-5,y=4-60+6,z=-5}, {name="default:glass"})	
	set_nodes_rdd(pos, {x=-31-60-2,y=4-60+1,z=4}, {x=-31-60-4,y=4-60+5,z=-4}, {name="air"})	
	set_nodes_rdd(pos, {x=-31-60-1,y=4-60  ,z=5}, {x=-31-60-5,y=4-60  ,z=-5}, {name="default:stone"})	
	minetest.set_node(vector.add(pos, {x=-31-60-4,y=4-60+1,z=-3}), {name="default:torch", param2=1}) 
	minetest.set_node(vector.add(pos, {x=-31-60-4,y=4-60+1,z= 0}), {name="default:torch", param2=1}) 
	minetest.set_node(vector.add(pos, {x=-31-60-4,y=4-60+1,z= 3}), {name="default:torch", param2=1}) 
end

local task_8_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
    local torches = 0
    local text
    for i=0,60 do
        local x=pos.x-31-i
        local floory=pos.y+4-i
        for z=pos.z-2,pos.z+2 do
        	for y=floory,floory+6 do
       			--print("x="..x.." y="..y.." z="..z.." floory="..floory.." pos.z="..pos.z.." i="..i)
        		local node=minetest.get_node({x=x, y=y, z=z})
        		if y==floory then
        			-- floor needs to be glass unless it is corner which doesn't matter
        			if z>pos.z-2 and z<pos.z+2 then
        				--not worried what bottom corners are
        				if node.name ~= "default:stone" then
							text = "Task 8 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but is floor so should be 'default:stone'"
							irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
							return false
						end
					end 
        		elseif y==floory+6 or z==pos.z+2 or z==pos.z-2 then
        			-- needs to be glass
					if node.name ~= "default:glass" then
						text = "Task 8 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but is roof or walls so should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end
        		elseif y==floory+1 and z==pos.z+1 then
	       			--print("   x="..x.." y="..y.." z="..z.." floory="..floory.." pos.z="..pos.z)
        			--can be torch or air
        			if node.name == "default:torch" then
        				torches = torches + 1
        			elseif node.name ~= "air" then
						text = "Task 8 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but is right side of tunnel on floor so should be 'default:torch' or 'air'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false        			
        			end
				elseif node.name ~= "air" then
					text = "Task 8 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but is middle of tunnel so should be 'air'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false        			
				end --if
        	end --for y
        end -- for z
	end -- for i
	if torches < 13 then
		text = "Task 8 Assessment\n \nOnly "..torches.." torches. Should be at least 13"
		irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
		return false        			        	
	elseif torches > 18 then
		text = "Task 8 Assessment\n \nCounted "..torches.." torches. Should be no more than 18"
		irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
		return false        			        	        	
	end
	text = "Task 8 Assessment\n \nCompleted"
	irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
    return true
end

local task_9_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
    -- open up subway to task 8 tunnel and give next task
    set_nodes_rdd(pos, {x=-31-61,y=5-60,z=-1}, {x=-31-61,y=9-60,z=1}, {name="air"})

	local pos_chest = vector.add(pos,{x=-31-61,y=5-60,z=0})
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nLook in chest at bottom of your tunnel"
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)

	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	text='Task 9 - Stairs and rail\n \n"stairs:stair_stonebrick"\n"carts:rail"\n"carts:powerrail"'
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
	
	text='Put rail and powered rail along centre of your tunnel. Where tunnel sloping place stairs down left side.'
	minetest.set_node(pos_chest, {name="default:chest",param2=3})
	irc_builder.add_book_to_chest(player_name, pos_chest, {title="Task 9 for "..player_name, text=text})
end
    
local task_9_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
    local torches = 0
    local text
    local node
    -- check stairs and rail in sloping section of tunnel
    for i=0,60 do
        local x=pos.x-31-i
        local floory=pos.y+4-i
        if i < 60 then
        	-- Don't need stairs on the last block
	        node=minetest.get_node({x=x, y=floory, z=pos.z-1})
			if node.name:find("stairs:") ~= 1 then
				text = "Task 9 Assessment\n \nBlock at ("..x..", "..floory..", "..(pos.z-1)..") is type '"..node.name.."' but should be 'stairs:stair_stonebrick' or similar"
				irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
				return false
			end
			if node.param2 ~= 1 then
				text = "Task 9 Assessment\n \nBlock at ("..x..", "..floory..", "..(pos.z-1)..") has param2 '"..node.param2.."' but should be 1 to be descending with negative x"
				irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
				return false
			end
		end
        node=minetest.get_node({x=x, y=floory+1, z=pos.z})
		if node.name ~= "carts:rail" and node.name ~= "carts:powerrail" then
			text = "Task 9 Assessment\n \nBlock at ("..x..", "..(floory+1)..", "..pos.z..") is type '"..node.name.."' but should be 'carts:rail' or 'carts:powerrail'"
			irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
			return false
		end
		-- TODO check enough powerrail
	end -- for i
	-- check rail in flat section of tunnel
	for x=pos.x-30,pos.x-7 do
		local node=minetest.get_node({x=x,y=pos.y+5,z=pos.z})
		if node.name ~= "carts:rail" and node.name ~= "carts:powerrail" then
			text = "Task 9 Assessment\n \nBlock at ("..x..", "..(pos.y+5)..", "..pos.z..") is type '"..node.name.."' but should be 'carts:rail' or 'carts:powerrail'"
			irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
			return false
		end
	end
	text = "Task 9 Assessment\n \nCompleted"
	irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
    return true
    -- TODO Task 10 put cart in chest so player can run cart from their tunnel to someone elses
end

local task_10_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_chest = vector.add(pos,{x=-31-61-3,y=5-60,z=-2})
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nLook in chest in subway for a cart"
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)

	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	text='Task 10 - Run a minecart from your tunnel to another tunnel. You may need to assist a neighbouring builder to finish their tunnel.'
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
    -- check tunnel to the left
	local node = minetest.get_node(vector.add(pos, {x=-31-60-3, y=4-60+1, z=-5}))
	if node.name == "default:obsidian_glass" then
        -- tunnel to the left is complete so safe to open up
        set_nodes_rdd(pos, {x=-31-60-2,y=4-60+1,z=-5}, {x=-31-60-4,y=4-60+5,z=-5}, {name="air"})
        minetest.set_node(vector.add(pos, {x=-31-60-3,y=4-60+1,z=-5}), {name="carts:rail"})
    else
        minetest.set_node(vector.add(pos, {x=-31-60-3,y=4-60+1,z=-5}), {name="default:obsidian_glass"})
    end
    -- check tunnel to the right
	local node = minetest.get_node(vector.add(pos, {x=-31-60-3, y=4-60+1, z=5}))
	if node.name == "default:obsidian_glass" then
        -- tunnel to the left is complete so safe to open up
        set_nodes_rdd(pos, {x=-31-60-2,y=4-60+1,z=5}, {x=-31-60-4,y=4-60+5,z=5}, {name="air"})
        minetest.set_node(vector.add(pos, {x=-31-60-3,y=4-60+1,z=5}), {name="carts:rail"})
    else
        minetest.set_node(vector.add(pos, {x=-31-60-3,y=4-60+1,z=5}), {name="default:obsidian_glass"})
    end
    -- build rail in subway
    set_nodes_rdd(pos, {x=-31-60-1,y=4-60+1,z=0}, {x=-31-60-2,y=4-60+1,z=0}, {name="carts:rail"})
    set_nodes_rdd(pos, {x=-31-60-3,y=4-60+1,z=-4}, {x=-31-60-3,y=4-60+1,z=4}, {name="carts:rail"})
    set_nodes_rdd(pos, {x=-31-60-3,y=4-60+1,z=-3}, {x=-31-60-3,y=4-60+1,z=-2}, {name="carts:powerrail"})
    set_nodes_rdd(pos, {x=-31-60-3,y=4-60+1,z=3}, {x=-31-60-3,y=4-60+1,z=2}, {name="carts:powerrail"})
    --mc.setBlock(x-31-60-4,y+4-60+1,z-2,block.TORCH_REDSTONE.id,5)
    --mc.setBlock(x-31-60-4,y+4-60+1,z+2,block.TORCH_REDSTONE.id,5)
    --mc.setBlock(x-31-60-4,y+4-60+1,z,69,13) #lever
    minetest.set_node(vector.add(pos, {x=-31-60-4,y=4-60+1,z=-4}), {name="default:torch", param2=1})
    minetest.set_node(vector.add(pos, {x=-31-60-4,y=4-60+1,z= 4}), {name="default:torch", param2=1})
    -- put cart in chest in subway
	local chest_name="default:chest"
	local chest_node=minetest.get_node(pos_chest)
	if chest_node.name ~= chest_name then
		minetest.set_node(pos_chest, {name=chest_name,param2=3})
	end
	local meta=minetest.get_meta(pos_chest)
	local invref = meta:get_inventory()
	invref:add_item("main",ItemStack("carts:cart"))
end

local task_10_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
    local text
	text = "Task 10 Assessment\n \nTask 10 is not a programming task, although you may need to assist your neighbour's programming task to complete"
	irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
    return true
end


builder_police.tasks={
	task_1_assign,
	task_2_assign,
	task_3_assign,
	task_4_assign,
	task_5_assign,
	task_6_assign,
	task_7_assign,
	task_8_assign,
	task_9_assign,
	task_10_assign,
}

builder_police.tests={
	task_1_test,
	task_2_test,
	task_3_test,
	task_4_test,
	task_5_test,
	task_6_test,
	task_7_test,
	task_8_test,
	task_9_test,
	task_10_test,
}

builder_police.jails={
	{p1={x=90, y=5, z=-5}, p2={x=110, y=20, z=5}}, --1
	{p1={x=90, y=5, z=-5}, p2={x=110, y=20, z=5}}, --2
	{p1={x=90, y=5, z=-5}, p2={x=110, y=20, z=5}}, --3
	{p1={x=90, y=5, z=-5}, p2={x=130, y=20, z=5}}, --4
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --5
	{p1={x=69, y=5, z=-5}, p2={x=130, y=32, z=5}}, --6
	{p1={x=69, y=5, z=-5}, p2={x=130, y=32, z=5}}, --7
	{p1={x=10, y=-60, z=-5}, p2={x=130, y=32, z=5}}, --8
	{p1={x=10, y=-60, z=-5}, p2={x=130, y=32, z=5}}, --9
	{p1={x=10, y=-60, z=-5}, p2={x=130, y=32, z=5}}, --10
}
		