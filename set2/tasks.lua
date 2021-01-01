
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

local assert_correct = function(player_name, task, x, y, z, correct_name, direction)
	local pos_build = builder_police.pos_build(player_name)
	local pos_assess = vector.add(pos_build, {x=0,y=0,z=1})
	local node=minetest.get_node({x=x,y=y,z=z})
	if node.name == "ignore" then
		-- map not available yet so ignore
		return false
	end
	if node.name ~= correct_name then
		local text = "Task "..task.." Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be '"..correct_name.."'"
		irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
		return false
	end
	if direction then
		local reg=minetest.registered_nodes[correct_name]
		local dira, dirb, correct_param2a, correct_param2b
		direction = direction:lower()
		if direction=="+x" then dira={x=1,y=0,z=0}
		elseif direction=="-x" then dira={x=-1,y=0,z=0}
		elseif direction=="+y" then dira={x=0,y=1,z=0}
		elseif direction=="-y" then dira={x=0,y=-1,z=0}
		elseif direction=="+z" then dira={x=0,y=0,z=1}
		elseif direction=="-z" then dira={x=0,y=0,z=-1}
		elseif direction=="x" then 
			dira={x=1, y=0, z=0}
			dirb={x=-1, y=0, z=0}
		elseif direction=="y" then
			dira={x=0, y=1, z=0}
			dirb={x=0, y=-1, z=0}
		elseif direction=="z" then
			dira={x=0, y=0, z=1}
			dirb={x=0, y=0, z=-1}
		end
		if reg.paramtype2=="wallmounted" then
			correct_param2a = minetest.dir_to_wallmounted(dira)
		elseif reg.paramtype2=="facedir" then 
			correct_param2a = minetest.dir_to_facedir(dira)
		end
		if dirb then
			if reg.paramtype2=="wallmounted" then
				correct_param2b = minetest.dir_to_wallmounted(dirb)
			elseif reg.paramtype2=="facedir" then 
				correct_param2b = minetest.dir_to_facedir(dirb)
			end
			if node.param2 ~= correct_param2a and node.param2 ~= correct_param2b then
				local text = "Task "..task.." Assessment\n \n"..correct_name.." at ("..x..", "..y..", "..z..") is direction '"..node.param2.."' but should be '"..correct_param2a.."' or '"..correct_param2b.."'"
				irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
				return false
			end
		else
			if node.param2 ~= correct_param2a then
				local text = "Task "..task.." Assessment\n \n"..correct_name.." at ("..x..", "..y..", "..z..") is direction '"..node.param2.."' but should be '"..correct_param2a.."'"
				irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
				return false
			end
		end
	end
	return true
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
	text="Place a green wool block at x,y,z coordinates above\n \nwool:green"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
end

local task_1_test = function(player_name)
	local pos_build = builder_police.pos_build(player_name)
	local pos = vector.add(pos_build, {x=0,y=4,z=0})
	if not assert_correct(player_name, 1, pos.x, pos.y, pos.z, "wool:green", nil) then
		return false
	end
	return true
end

local task_2_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	text="Place a blue wool block at x,y,z coordinates above\n \nwool:blue"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
end

local task_2_test = function(player_name)
	local pos_build = builder_police.pos_build(player_name)
	local pos = vector.add(pos_build, {x=0,y=4,z=0})
	if not assert_correct(player_name, 1, pos.x, pos.y, pos.z, "wool:blue", nil) then
		return false
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
	local text="Place a glass frame around block of red wool at coordinates above. All glass blocks are to have same x value.\n \ndefault:glass"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
end

local task_3_test = function(player_name)
	local pos_build = builder_police.pos_build(player_name)
	local pos = vector.add(pos_build, {x=0,y=4,z=0})
	local correct_name
	for y=pos.y-1,pos.y+1 do
		for z=pos.z-1,pos.z+1 do
			if z == pos.z and y == pos.y then
				correct_name = "wool:red"
			else
				correct_name = "default:glass"
			end
			if not assert_correct(player_name, 3, pos.x, y, z, correct_name, nil) then
				return false
			end
		end
	end
	return true
end

--Task 3a
local task_4_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	local text="Place a 3 x 3 obsidian glass square at x=99, same y and z.\n \ndefault:obsidian_glass"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
end

local task_4_test = function(player_name)
	local pos_build = builder_police.pos_build(player_name)
	local pos = vector.add(pos_build, {x=0,y=4,z=0})
	local x = pos.x - 1
	for y=pos.y-1,pos.y+1 do
		for z=pos.z-1,pos.z+1 do
			if not assert_correct(player_name, 4, x, y, z, "default:obsidian_glass", nil) then
				return false
			end
		end
	end
	return true
end

--Task 3b
local task_5_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	local text="Place an obsidian glass square at x=101, same y and z.\n \ndefault:obsidian_glass"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
end

local task_5_test = function(player_name)
	local pos_build = builder_police.pos_build(player_name)
	local pos = vector.add(pos_build, {x=0,y=4,z=0})
	local x = pos.x + 1
	for y=pos.y-1,pos.y+1 do
		for z=pos.z-1,pos.z+1 do
			if not assert_correct(player_name, 5, x, y, z, "default:obsidian_glass", nil) then
				return false
			end
		end
	end
	return true
end

--Task 3c
local task_6_assign = function(player_name)
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

local task_6_test = function(player_name)
	local pos_build = builder_police.pos_build(player_name)
	local pos = vector.add(pos_build, {x=0,y=4,z=0})
	local correct_name
	for x=pos.x-1,pos.x+1 do
		for y=pos.y-1,pos.y+1 do
			for z=pos.z-1,pos.z+1 do
				local node = minetest.get_node({x=x,y=y,z=z})
				if x == pos.x and z == pos.z and y == pos.y then
					correct_name = "wool:yellow"
				else
					correct_name = "default:glass"
				end
				if not assert_correct(player_name, 6, x, y, z, correct_name, nil) then
					return false
				end
			end
		end
	end
	return true
end

--Task 4
local task_7_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	-- first clear air for tasks chequered square and chequered diamond6 and 7
	set_nodes_rdd(pos, {x=-10,y=12,z=-5},    {x=10,y=32,z=4},    {name="air"})
	-- assign task 7
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	local text="Climb down the ladder below this sign to see task 7"
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

local task_7_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	for x=pos.x-30,pos.x-7 do
		for y=pos.y+4,pos.y+10 do
			for z=pos.z-2,pos.z+2 do
				local node=minetest.get_node({x=x,y=y,z=z})
				if node.name == "ignore" then
					return false
				elseif y==pos.y+4 then
					-- floor should be glass or stone
					if node.name ~= "default:glass" and node.name ~= "default:stone" then
						local text = "Task 7 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end				
				elseif z==pos.z-2 or z==pos.z+2 or y==pos.y+10 then
					-- side walls and roof should be glass
					if node.name ~= "default:glass" then
						local text = "Task 7 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end
				elseif y==pos.y+5 then
					--above floor should be air or torches
					if node.name ~= "air" and node.name:find("default:torch") ~= 1 then
						local text = "Task 7 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end				
				elseif node.name ~= "air" then
					text = "Task 7 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false				
				end
			end
		end
	end
	return true
end
--Task 5
local task_8_assign = function(player_name)
	-- Task 5 automatically assigned when task 4 completed but repeated in case accidentally deleted
	local pos = builder_police.pos_build(player_name) 
	local sign_pos=vector.add(pos,{x=-18,y=6,z=-3})
	local text="Congratulations "..player_name.."\n \nNow change the tunnel floor to stone and place a torch every 4 blocks"
	irc_builder.set_sign(sign_pos, "-z", "default:sign_wall_wood", text)
end

local task_8_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	local torches = 0
	for x=pos.x-30,pos.x-7 do
		for y=pos.y+4,pos.y+5 do
			for z=pos.z-1,pos.z+1 do
				local node=minetest.get_node({x=x,y=y,z=z})
				if node.name == "ignore" then
					return false
				elseif y==pos.y+4 then
					-- floor should be stone
					if node.name ~= "default:stone" then
						local text = "Task 8 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:stone'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end				
				else
					-- side walls and roof should be glass
					if node.name:find("default:torch") == 1 then
						torches = torches + 1
					elseif node.name ~= "air" then
						local text = "Task 8 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air' or 'default:torch'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end	
				end			
			end
		end
	end
	local text = "Task 8 Assessment\n \nCompleted"
	irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
	return true
end
--Task Wall of glass
local task_9_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	local text="Climb down the ladder below this sign to see task 9"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
	set_nodes_rdd(pos, {x=-1,y=-1,z=-1},  {x=20,y=-5,z=1},    {name="default:stone"})
	set_nodes_rdd(pos, {x=1,y=-1,z=0},    {x=1,y=-4,z=0},     {name="default:ladder_wood", param2=minetest.dir_to_wallmounted({x=-1,y=0,z=0})})
	set_nodes_rdd(pos, {x=2,y=-2,z=0},    {x=19,y=-4,z=0},    {name="air"})
	for torchx=pos.x+2,pos.x+19,4 do
		minetest.set_node({x=torchx, y=pos.y-4, z=pos.z}, {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	end
	sign_pos=vector.add(pos,{x=12,y=-3,z=0})
	text="Hello "..player_name.."\n \nYour task is to create a glass wall with external dimensions of 5 blocks wide and 7 blocks high"
	irc_builder.set_sign(sign_pos, "+z", "default:sign_wall_wood", text)
	sign_pos=vector.add(pos,{x=16,y=-3,z=0})
	text="Centre of wall floor has coordinates \nx1="..(pos.x+5).." y="..(pos.y-1).." z="..pos.z
	irc_builder.set_sign(sign_pos, "+z", "default:sign_wall_wood", text)
end

local task_9_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	for x=pos.x+5,pos.x+5 do
		for y=pos.y-1,pos.y+5 do
			for z=pos.z-2,pos.z+2 do
				local node=minetest.get_node({x=x,y=y,z=z})
				if node.name == "ignore" then
					return false
				elseif y==pos.y-1 then
					-- floor should be glass or stone
					if node.name ~= "default:glass" and node.name ~= "default:stone" then
						local text = "Task 9 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end				
				else
					-- wall should be glass
					if node.name ~= "default:glass" then
						local text = "Task 9 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end
				end
			end
		end
	end
	return true
end

--Task Arch
local task_10_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	local text="Make an arch by removing 15 glass blocks from middle of wall"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
end

local task_10_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	for x=pos.x+5,pos.x+5 do
		for y=pos.y-1,pos.y+5 do
			for z=pos.z-2,pos.z+2 do
				local node=minetest.get_node({x=x,y=y,z=z})
				if node.name == "ignore" then
					return false
				elseif y==pos.y-1 then
					-- floor should be glass or stone
					if node.name ~= "default:glass" and node.name ~= "default:stone" then
						local text = "Task 10 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end				
				elseif z==pos.z-2 or z==pos.z+2 or y==pos.y+5 then
					-- side walls and roof should be glass
					if node.name ~= "default:glass" then
						local text = "Task 10 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end
				elseif y==pos.y then
					--above floor should be air or torches
					if node.name ~= "air" and node.name:find("default:torch") ~= 1 then
						local text = "Task 10 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end				
				elseif node.name ~= "air" then
					text = "Task 10 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false				
				end
			end
		end
	end
	return true
end

--Task Arch floor
local task_11_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	local text="Replace arch floor with stone and place one torch on the stone\n \ndefault:stone"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
end

local task_11_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	local torches = 0
	for x=pos.x+5,pos.x+5 do
		for y=pos.y-1,pos.y+5 do
			for z=pos.z-2,pos.z+2 do
				local node=minetest.get_node({x=x,y=y,z=z})
				if node.name == "ignore" then
					return false
				elseif y==pos.y-1 then
					-- floor should be glass or stone on edges
					if z==pos.z-2 or z==pos.z+2 then
						if node.name ~= "default:glass" and node.name ~= "default:stone" then
							local text = "Task 11 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
							irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
							return false
						end
					else
						--floor should be stone in middle
						if node.name ~= "default:stone" then
							local text = "Task 11 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:stone'"
							irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
							return false
						end
					end
				elseif z==pos.z-2 or z==pos.z+2 or y==pos.y+5 then
					-- side walls and roof should be glass
					if node.name ~= "default:glass" then
						local text = "Task 11 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end
				elseif y==pos.y then
					--above floor should be air or torches
					if node.name ~= "air" and node.name:find("default:torch") ~= 1 then
						local text = "Task 11 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air' or 'default:torch'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end
					if node.name:find("default:torch") == 1 then
						torches = torches + 1
					end
				elseif node.name ~= "air" then
					text = "Task 11 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false				
				end
			end
		end
	end
	if torches ~= 1 then
		text = "Task 11 Assessment\n \nNumber of torches is "..torches.." but should be 1"
		irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
		return false				
	end
	return true
end

--Task Arches
local task_12_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	local text="Repeat arches every four blocks from x=105 to x=117"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
end

local task_12_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	local torches = 0
	for x=pos.x+5,pos.x+17,4 do
		for y=pos.y-1,pos.y+5 do
			for z=pos.z-2,pos.z+2 do
				local node=minetest.get_node({x=x,y=y,z=z})
				if node.name == "ignore" then
					return false
				elseif y==pos.y-1 then
					-- floor should be glass or stone on edges
					if z==pos.z-2 or z==pos.z+2 then
						if node.name ~= "default:glass" and node.name ~= "default:stone" then
							local text = "Task 12 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
							irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
							return false
						end
					else
						--floor should be stone in middle
						if node.name ~= "default:stone" then
							local text = "Task 12 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:stone'"
							irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
							return false
						end
					end
				elseif z==pos.z-2 or z==pos.z+2 or y==pos.y+5 then
					-- side walls and roof should be glass
					if node.name ~= "default:glass" then
						local text = "Task 12 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end
				elseif y==pos.y then
					--above floor should be air or torches
					if node.name ~= "air" and node.name:find("default:torch") ~= 1 then
						local text = "Task 12 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air' or 'default:torch'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end
					if node.name:find("default:torch") == 1 then
						torches = torches + 1
					end
				elseif node.name ~= "air" then
					text = "Task 12 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false				
				end
			end
		end
		if torches ~= 1 then
			text = "Task 12 Assessment\n \nNumber of torches is "..torches.." at x="..x.." but should be 1"
			irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
			return false				
		end
		torches = 0
	end
	return true
end

--Task Castle base
local task_13_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	local text="Castle base: Create a 9 x 5 x 5 open top stone box starting at x=121, y=9. Add a 2 block high doorway at x=121."
	local sign_task_pos={x=pos.x+5,y=pos.y+1,z=pos.z+1}
	irc_builder.set_sign(sign_task_pos, "+z", "default:sign_wall_wood", text)
end

local task_13_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	for x=121,129 do
		for y=9,13 do
			for z=pos.z-2,pos.z+2 do
				local node=minetest.get_node({x=x,y=y,z=z})
				if node.name == "ignore" then
					-- map not available yet so ignore
					return false
				end
				local correct_block = "air"
				if x==121 and (y==10 or y==11) and z==pos.z then
					-- doorway should be air
					correct_block = "air"
				elseif y==pos.y-1 or z==pos.z-2 or z==pos.z+2 or x==129 or x==121 then
					-- floor and wall should be stone on edges
					correct_block = "default:stone"
				end
				if node.name ~= correct_block then
					local text = "Task 13 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be '"..correct_block.."'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false
				end
			end
		end
	end
	return true
end

--Task Castle windows
local task_14_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	local text="Castle windows: Create 3 bar windows 3 blocks high on side of castle and 1 bar window 3 blocks wide above doorway"
	local sign_task_pos={x=pos.x+9,y=pos.y+1,z=pos.z+1}
	irc_builder.set_sign(sign_task_pos, "+z", "default:sign_wall_wood", text)
end

local task_14_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	local correct_name = "xpanes:bar_flat"
	local reg=minetest.registered_nodes[correct_name]
	local correct_param2a
	local correct_param2b
	local dira = {x=0,y=0,z=1}
	local dirb = {x=0,y=0,z=-1}
	if reg.paramtype2=="wallmounted" then
		correct_param2a = minetest.dir_to_wallmounted(dira)
		correct_param2b = minetest.dir_to_wallmounted(dirb)
	elseif reg.paramtype2=="facedir" then 
		correct_param2a = minetest.dir_to_facedir(dira)
		correct_param2b = minetest.dir_to_facedir(dirb)
	end
	for x = 123, 127, 2 do
		for y = 11, 13 do
			for z=pos.z-2, pos.z+2, 4 do
				local node=minetest.get_node({x=x,y=y,z=z})
				if node.name == "ignore" then
					-- map not available yet so ignore
					return false
				end
				if node.name ~= correct_name then
					local text = "Task 14 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be '"..correct_name.."'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false
				end
				if node.param2 ~= correct_param2a and node.param2 ~= correct_param2b then
					local text = "Task 14 Assessment\n \n"..correct_name.." at ("..x..", "..y..", "..z..") is direction '"..node.param2.."' but should be '"..correct_param2a.."' or '"..correct_param2b.."'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false
				end
			end
		end
	end
	local dira = {x=1,y=0,z=0}
	local dirb = {x=-1,y=0,z=0}
	if reg.paramtype2=="wallmounted" then
		correct_param2a = minetest.dir_to_wallmounted(dira)
		correct_param2b = minetest.dir_to_wallmounted(dirb)
	elseif reg.paramtype2=="facedir" then 
		correct_param2a = minetest.dir_to_facedir(dira)
		correct_param2b = minetest.dir_to_facedir(dirb)
	end
	local x = 121
	local y = 13
	for z=pos.z-1, pos.z+1 do
		local node=minetest.get_node({x=x,y=y,z=z})
		if node.name == "ignore" then
			-- map not available yet so ignore
			return false
		end
		if node.name ~= correct_name then
			local text = "Task 14 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be '"..correct_name.."'"
			irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
			return false
		end
		if node.param2 ~= correct_param2a and node.param2 ~= correct_param2b then
			local text = "Task 14 Assessment\n \n"..correct_name.." at ("..x..", "..y..", "..z..") is direction '"..node.param2.."' but should be '"..correct_param2a.."' or '"..correct_param2b.."'"
			irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
			return false
		end
	end
	return true
end

--Task Castle roof
local task_15_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	local text="Castle roof: Add a 11 x 7 x 3 open top stone box on top of the castle base to be the roof. Add a ladder so that players can climb up the ladder to the roof x=128, z="..pos.z
	local sign_task_pos={x=pos.x+13,y=pos.y+1,z=pos.z+1}
	irc_builder.set_sign(sign_task_pos, "+z", "default:sign_wall_wood", text)
end

local task_15_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local ladder_name = "default:ladder_wood"
	local correct_name
	for x = 120, 130 do
		for y = 14, 15, 16 do
			for z = pos.z-3, pos.z+3 do
				if x==128 and y==14 and z==pos.z then
					correct_name = ladder_name 
				elseif x==120 or x==130 or y==14 or z==pos.z-3 or z==pos.z+3 then
					correct_name = "default:stone"
				else
					correct_name = "air"
				end
				local correct_direction = nil
				if correct_name == ladder_name then
					correct_direction = "+x"
				end
				if not assert_correct(player_name, 15, x, y, z, correct_name, correct_direction) then
					return false
				end
			end
		end
	end
	local x = 128
	local z = pos.z
	for y = 10, 14 do
		if not assert_correct(player_name, 15, x, y, z, ladder_name, "+x") then
			return false
		end
	end
	return true
end

--Task Castle
local task_16_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	local text="Castle: Add a door in doorway, crenels in the roof, and a red carpet under the arches to the ladder"
	local sign_task_pos={x=pos.x+17,y=pos.y+1,z=pos.z+1}
	irc_builder.set_sign(sign_task_pos, "+z", "default:sign_wall_wood", text)
end

local task_16_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local correct_name
	for x = 121, 129, 2 do
		for y = 16, 16 do
			for z=pos.z-2, pos.z+2, 2 do
				if not assert_correct(player_name, 16, x, y, z, "air", nil) then 
					return false
				end
			end
		end
	end
	for x = 105, 128 do
		for y = 9, 9 do
			for z=pos.z, pos.z do
				if not assert_correct(player_name, 16, x, y, z, "wool:red", nil) then 
					return false
				end
			end
		end
	end
	for x = 121, 121 do
		for y = 10, 11 do
			for z=pos.z, pos.z do
				if not assert_correct(player_name, 16, x, y, z, "doors:door_wood_a", "+x") then 
					return false
				end
			end
		end
	end
	return true
end

--Task Flag
local task_17_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local text=player_name.."\n \nx="..pos.x..'\ny='..(pos.y+4)..'\nz='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)
	local text="Add a pole at x=122, y=15 with a 21 x 13 flag at y=22"
	local sign_task_pos={x=pos.x+1,y=pos.y,z=pos.z}
	irc_builder.set_sign(sign_task_pos, "-x", "default:sign_wall_wood", text)
end

local task_17_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local correct_name
	for x = 122, 122 do
		for y = 15, 21 do
			for z=pos.z, pos.z do
				if not assert_correct(player_name, 17, x, y, z, "default:fence_junglewood", nil) then 
					return false
				end
			end
		end
	end
	for x = 122, 122 do
		for y = 22, 22 do
			for z=pos.z, pos.z do
				if not assert_correct(player_name, 17, x, y, z, "wool:", nil) then 
					return false
				end
			end
		end
	end
	return true
end


--Task 6 chequered square
local task_18_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	-- local pos_chest = vector.add(pos,{x=-31,y=5,z=0})
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.." Task 18\n \nChequered Square"
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)

	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	text='Construct a vertical square shape of alternating wool colours in the sky with height of 9 blocks with centre at\nx='..pos.x..' y='..(pos.y+22)..' z='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)	
end

local task_18_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	local z = pos.z
	for y=pos.y+18,pos.y+26 do
		local prev = ""
		for x=pos.x-4,pos.x+4 do
			local node=minetest.get_node({x=x,y=y,z=z})
			if node.name == "ignore" then
				return false
			end
			if node.name == prev then
				local text = "Task 18 Assessment\n \nBlocks at ("..(x-1)..", "..y..", "..z..") and ("..x..", "..y..", "..z..") are both of type '"..node.name.."' but should be different if alternating"
				irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
				return false
			end
			prev = node.name
			if node.name:find('wool') ~= 1 then
				local text = "Task 18 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be a wool type, eg 'wool:orange'"
				irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
				return false
			end	
		end
	end			
	local text = "Task 18 Assessment\n \nCompleted"
	irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
	return true
end

-- Task 7 Chequered Diamond
local task_19_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	-- local pos_chest = vector.add(pos,{x=-31,y=5,z=0})
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.." Task 19\n \nChequered Diamond"
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)

	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	text='Construct a 2D diamond shape of alternating wool colours in the sky with height of 21 blocks with centre at\nx='..pos.x..' y='..(pos.y+22)..' z='..pos.z
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)	
end

local task_19_test = function(player_name)
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
			if node.name == "ignore" then
				return false
			end
			if i<woolmin or i> woolmax then
				if node.name ~= "air" then
					local text = "Task 19 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be 'air'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false
				end	
			else
				if node.name == prev then
					local text = "Task 19 Assessment\n \nBlocks at ("..(x-1)..", "..y..", "..z..") and ("..x..", "..y..", "..z..") are both of type '"..node.name.."' but should be different if alternating"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false
				end
				prev = node.name
				if node.name:find('wool') ~= 1 then
					local text = "Task 19 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but should be a wool type, eg 'wool:orange'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false
				end	
			end
		end
	end			
	local text = "Task 19 Assessment\n \nCompleted"
	irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
	return true
end

-- Task 8 Sloping tunnel
local task_20_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_chest = vector.add(pos,{x=-31,y=5,z=0})
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nLook in chest in your tunnel"
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)

	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	text="Task 20\n \nSloping tunnel\n \nSee book"
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
	
	set_nodes_rdd(pos, {x=-31,y=4,z=-2}, {x=-33,y=10,z=2}, {name="default:meselamp"})	
	set_nodes_rdd(pos, {x=-31,y=5,z=-1}, {x=-31,y= 9,z=1}, {name="air"})	
	text='Continue glass tunnel down on a diagonal where centre of tunnel floor goes from x1='..(pos.x-31)..',y1='..(pos.y+4)..' to x2='..(pos.x-31-60)..',y2='..(pos.y+4-60)..'. z is constant z='..pos.z..'. Make sure no lava or water leak into tunnel'
	minetest.set_node(pos_chest, {name="default:chest",param2=3})
	irc_builder.add_book_to_chest(player_name, pos_chest, {title="Task 20 for "..player_name, text=text})

    -- check tunnel to the left and right for obsidian_glass which means neighbour up to task 10
	local node_left = minetest.get_node(vector.add(pos, {x=-31-60-3, y=4-60+1, z=-5}))
	local node_right = minetest.get_node(vector.add(pos, {x=-31-60-3, y=4-60+1, z=5}))

	set_nodes_rdd(pos, {x=-31-60-1,y=4-60  ,z=5}, {x=-31-60-5,y=4-60+6,z=-5}, {name="default:glass"})	
	set_nodes_rdd(pos, {x=-31-60-2,y=4-60+1,z=4}, {x=-31-60-4,y=4-60+5,z=-4}, {name="air"})	
	set_nodes_rdd(pos, {x=-31-60-1,y=4-60  ,z=5}, {x=-31-60-5,y=4-60  ,z=-5}, {name="default:stone"})	
	minetest.set_node(vector.add(pos, {x=-31-60-4,y=4-60+1,z=-3}), {name="default:torch", param2=1}) 
	minetest.set_node(vector.add(pos, {x=-31-60-4,y=4-60+1,z= 0}), {name="default:torch", param2=1}) 
	minetest.set_node(vector.add(pos, {x=-31-60-4,y=4-60+1,z= 3}), {name="default:torch", param2=1}) 
	
	if node_left.name == "wool:green" then
        -- tunnel to the left is complete so safe to open up. Re-place green which we set to glass above
        set_nodes_rdd(pos, {x=-31-60-2,y=4-60+1,z=-5}, {x=-31-60-4,y=4-60+5,z=-5}, {name="air"})
        minetest.set_node(vector.add(pos, {x=-31-60-3,y=4-60+1,z=-5}), {name="wool:green"})
    end
    -- check tunnel to the right
	if node_right.name == "wool:red" then
        -- tunnel to the right is complete so safe to open up. Re-place red which we set to glass above
        set_nodes_rdd(pos, {x=-31-60-2,y=4-60+1,z=5}, {x=-31-60-4,y=4-60+5,z=5}, {name="air"})
        minetest.set_node(vector.add(pos, {x=-31-60-3,y=4-60+1,z=5}), {name="wool:red"})
    end

end

local task_20_test = function(player_name)
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
        		if node.name == "ignore" then
					return false
				elseif y==floory then
        			-- floor needs to be glass unless it is corner which doesn't matter
        			if z>pos.z-2 and z<pos.z+2 then
        				--not worried what bottom corners are
        				if node.name ~= "default:stone" then
							text = "Task 20 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but is floor so should be 'default:stone'"
							irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
							return false
						end
					end 
        		elseif y==floory+6 or z==pos.z+2 or z==pos.z-2 then
        			-- needs to be glass
					if node.name ~= "default:glass" then
						text = "Task 20 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but is roof or walls so should be 'default:glass'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false
					end
        		elseif y==floory+1 and z==pos.z+1 then
	       			--print("   x="..x.." y="..y.." z="..z.." floory="..floory.." pos.z="..pos.z)
        			--can be torch or air
        			if node.name == "default:torch" then
        				torches = torches + 1
        			elseif node.name ~= "air" then
						text = "Task 20 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but is right side of tunnel on floor so should be 'default:torch' or 'air'"
						irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
						return false        			
        			end
				elseif node.name ~= "air" then
					text = "Task 20 Assessment\n \nBlock at ("..x..", "..y..", "..z..") is type '"..node.name.."' but is middle of tunnel so should be 'air'"
					irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
					return false        			
				end --if
        	end --for y
        end -- for z
	end -- for i
	if torches < 13 then
		text = "Task 20 Assessment\n \nOnly "..torches.." torches. Should be at least 13"
		irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
		return false        			        	
	elseif torches > 18 then
		text = "Task 20 Assessment\n \nCounted "..torches.." torches. Should be no more than 18"
		irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
		return false        			        	        	
	end
	text = "Task 20 Assessment\n \nCompleted"
	irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
    return true
end
--Task 9 Stairs and rail
local task_21_assign = function(player_name)
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
	text='Task 21 - Stairs and rail\n \n"stairs:stair_stonebrick"\n"carts:rail"\n"carts:powerrail"'
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
	
	text='Put rail and powered rail along centre of your tunnel. Where tunnel sloping place stairs down left side.'
	minetest.set_node(pos_chest, {name="default:chest",param2=3})
	irc_builder.add_book_to_chest(player_name, pos_chest, {title="Task 9 for "..player_name, text=text})
end
    
local task_21_test_from_pos = function(pos)
	--local pos = builder_police.pos_build(player_name) 
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
	        if node.name == "ignore" then
				return false
			end
			if node.name:find("stairs:") ~= 1 then
				text = "Task 21 Assessment\n \nBlock at ("..x..", "..floory..", "..(pos.z-1)..") is type '"..node.name.."' but should be 'stairs:stair_stonebrick' or similar"
				return false, text
			end
			if node.param2 ~= 1 then
				text = "Task 21 Assessment\n \nBlock at ("..x..", "..floory..", "..(pos.z-1)..") has param2 '"..node.param2.."' but should be 1 to be descending with negative x"
				return false, text
			end
		end
        node=minetest.get_node({x=x, y=floory+1, z=pos.z})
		if node.name == "ignore" then
			return false
		end
		if node.name ~= "carts:rail" and node.name ~= "carts:powerrail" then
			text = "Task 21 Assessment\n \nBlock at ("..x..", "..(floory+1)..", "..pos.z..") is type '"..node.name.."' but should be 'carts:rail' or 'carts:powerrail'"
			return false, text
		end
		-- TODO check enough powerrail
	end -- for i
	-- check rail in flat section of tunnel
	for x=pos.x-30,pos.x-7 do
		local node=minetest.get_node({x=x,y=pos.y+5,z=pos.z})
		if node.name == "ignore" then
			return false, "ignore"
		end
		if node.name ~= "carts:rail" and node.name ~= "carts:powerrail" then
			text = "Task 21 Assessment\n \nBlock at ("..x..", "..(pos.y+5)..", "..pos.z..") is type '"..node.name.."' but should be 'carts:rail' or 'carts:powerrail'"
			return false, text
		end
	end
	text = "Task 9 Assessment\n \nCompleted"
    return true, text
end

local task_21_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
	local success, text = task_21_test_from_pos(pos)
	if text ~= "ignore" then
		irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
	end
	return success
end
--Task 10 Run minecart
local task_22_assign = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_chest = vector.add(pos,{x=-31-61-3,y=5-60,z=-2})
	minetest.set_node(pos, {name="default:stone"})
	minetest.set_node(vector.add(pos,{x=0,y=0,z=-1}), {name="default:torch_wall", param2=minetest.dir_to_wallmounted({x=0,y=0,z=1})})
	local sign_pos={x=pos.x,y=pos.y+1,z=pos.z}
	local text=player_name.."\n \nLook in chest in subway for a cart"
	irc_builder.set_sign(sign_pos, "-x", "signs:sign_yard", text)

	sign_pos={x=pos.x+1,y=pos.y,z=pos.z}
	text='Task 22 - Run a minecart from your tunnel to another tunnel. You may need to assist a neighbouring builder to finish their tunnel.'
	irc_builder.set_sign(sign_pos, "-x", "default:sign_wall_wood", text)
    -- check tunnel to the left
	local node = minetest.get_node(vector.add(pos, {x=-31-60-3, y=4-60+1, z=-5}))
	if node.name == "wool:green" then
        -- tunnel to the left is complete so safe to open up
        set_nodes_rdd(pos, {x=-31-60-2,y=4-60+1,z=-5}, {x=-31-60-4,y=4-60+5,z=-5}, {name="air"})
        minetest.set_node(vector.add(pos, {x=-31-60-3,y=4-60+1,z=-5}), {name="carts:rail"})
    else
        minetest.set_node(vector.add(pos, {x=-31-60-3,y=4-60+1,z=-5}), {name="wool:red"})
    end
    -- check tunnel to the right
	local node = minetest.get_node(vector.add(pos, {x=-31-60-3, y=4-60+1, z=5}))
	if node.name == "wool:red" then
        -- tunnel to the right is complete so safe to open up
        set_nodes_rdd(pos, {x=-31-60-2,y=4-60+1,z=5}, {x=-31-60-4,y=4-60+5,z=5}, {name="air"})
        minetest.set_node(vector.add(pos, {x=-31-60-3,y=4-60+1,z=5}), {name="carts:rail"})
    else
        minetest.set_node(vector.add(pos, {x=-31-60-3,y=4-60+1,z=5}), {name="wool:green"})
    end
    -- build rail in subway
    set_nodes_rdd(pos, {x=-31-60-1,y=4-60+1,z=0}, {x=-31-60-2,y=4-60+1,z=0}, {name="carts:rail"})
    set_nodes_rdd(pos, {x=-31-60-3,y=4-60+1,z=-4}, {x=-31-60-3,y=4-60+1,z=4}, {name="carts:rail"})
    set_nodes_rdd(pos, {x=-31-60-3,y=4-60+1,z=-3}, {x=-31-60-3,y=4-60+1,z=-2}, {name="carts:powerrail"})
    set_nodes_rdd(pos, {x=-31-60-3,y=4-60+1,z=3}, {x=-31-60-3,y=4-60+1,z=2}, {name="carts:powerrail"})
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
	-- Build ladder and walkway to task 11
	local z11 = pos.z
	local x11 = pos.x - 200 + (math.floor(z11/10) % 2) * 50
	local y11 = irc_builder.get_ground_level(x11, z11)
	minetest.set_node({x=x11, y=y11, z=z11}, {name="default:goldblock"})
	local x10 = pos.x - 25
	local y10 = pos.y + 4
	local z10 = pos.z
	local ramp = math.abs(y11-y10) --length of sloping ramp between levels
	-- small tunnel to go around sloping part of tunnel
	set_nodes({x=x10+ 2, y=y10  , z=z10-2}, {x=x10-22, y=y10+6, z=z10-6}, {name="default:glass"})
	set_nodes({x=x10+ 1, y=y10  , z=z10-3}, {x=x10-21, y=y10  , z=z10-5}, {name="default:stone"})
	set_nodes({x=x10+ 1, y=y10  , z=z10-2}, {x=x10- 3, y=y10  , z=z10-2}, {name="default:stone"})
	set_nodes({x=x10-17, y=y10  , z=z10-2}, {x=x10-21, y=y10  , z=z10-2}, {name="default:stone"})
	set_nodes({x=x10+ 1, y=y10+1, z=z10-3}, {x=x10-21, y=y10+5, z=z10-5}, {name="air"})
	set_nodes({x=x10+ 1, y=y10+1, z=z10-2}, {x=x10- 3, y=y10+5, z=z10-2}, {name="air"})
	set_nodes({x=x10-17, y=y10+1, z=z10-2}, {x=x10-21, y=y10+5, z=z10-2}, {name="air"})
	set_nodes({x=x10-17, y=y10  , z=z10-1}, {x=x10-23, y=y10  , z=z10+1}, {name="default:stone"})
	set_nodes({x=x10-17, y=y10+1, z=z10-1}, {x=x10-23, y=y10+5, z=z10+1}, {name="air"})
	for i=3,16,4 do
		minetest.set_node({x=x10-i,y=y10+1,z=z10-3}, {name="default:torch",param2=1})
	end
	for i=17,22,4 do
		minetest.set_node({x=x10-i,y=y10+1,z=z10+1}, {name="default:torch",param2=1})
	end
	local stepy=(y10<=y11) and 1 or -1
	print("y10 "..y10.." y11 "..y11)
	local stair
	for i=1,ramp do
		local x = x10-23-i
		local y = y10+i*stepy
		print("x "..x.." y "..y)
		set_nodes({x=x, y=y  , z=z10-1}, {x=x, y=y  , z=z10+1}, {name="default:stone"})
		set_nodes({x=x, y=y+1, z=z10-1}, {x=x, y=y+5, z=z10+1}, {name="air"})
		if x%4 == 0 then
			minetest.set_node({x=x, y=y+1, z=z10+1}, {name="default:torch",param2=1})
		end
	end	
	if stepy > 0 then
		stair = {name="stairs:stair_stonebrick", param2="3"}
		for i=1,ramp do
			minetest.set_node({x=x10-23-i, y=y10+i*stepy  , z=z10-1}, stair)
		end
	else
		stair = {name="stairs:stair_stonebrick", param2="1"}
		for i=0,ramp-1 do
			minetest.set_node({x=x10-23-i, y=y10+i*stepy  , z=z10-1}, stair)
		end
	end
	set_nodes({x=x10-23-ramp-1, y=y11  , z=z11-1}, {x=x11+1, y=y11  , z=z11+1}, {name="default:stone"})
	set_nodes({x=x10-23-ramp-1, y=y11+1, z=z11-1}, {x=x11+1, y=y11+5, z=z11+1}, {name="air"})
	for x=x11+1,x10-23-ramp-1 do
		if x%4 == 0 then
			minetest.set_node({x=x, y=y11+1, z=z10+1}, {name="default:torch",param2=1})
		end
	end	
end

local task_22_test = function(player_name)
	local pos = builder_police.pos_build(player_name) 
	local pos_assess = vector.add(pos, {x=0,y=0,z=1})
    local text
	text = "Task 22 Assessment\n \nTask 10 is not a programming task, although you may need to assist your neighbour's programming task to complete."
	local pos_left = vector.add(pos, {x=0, y=0, z=-builder_police.get_delta_z()})
	local pos_right = vector.add(pos, {x=0, y=0, z=-builder_police.get_delta_z()})
	local test_left, message_left = task_9_test_from_pos(pos_left) 
	local test_right, message_right = task_9_test_from_pos(pos_right) 
	local test = test_left or test_right
	if test then 
		text = text .. " Well done! One of your neighbours has also completed Task 9."
	else
		text = text .. " Currently neither of your neighbours has completed Task 9."
	end
	irc_builder.set_sign(pos_assess, "-z", "default:sign_wall_wood", text)
    return test
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
	task_11_assign,
	task_12_assign,
	task_13_assign,
	task_14_assign,
	task_15_assign,
	task_16_assign,
	task_17_assign,
	task_18_assign,
	task_19_assign,
	task_20_assign,
	task_21_assign,
	task_22_assign,
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
	task_11_test,
	task_12_test,
	task_13_test,
	task_14_test,
	task_15_test,
	task_16_test,
	task_17_test,
	task_18_test,
	task_19_test,
	task_20_test,
	task_21_test,
	task_22_test,
}

builder_police.jails={
	{p1={x=90, y=5, z=-5}, p2={x=110, y=20, z=5}}, --1
	{p1={x=90, y=5, z=-5}, p2={x=110, y=20, z=5}}, --2
	{p1={x=90, y=5, z=-5}, p2={x=110, y=20, z=5}}, --3
	{p1={x=90, y=5, z=-5}, p2={x=130, y=20, z=5}}, --4
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --5
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --6 5
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --7 5
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --8 5
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --9 5
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --10 5
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --11 5
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --12 5
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --13 5 
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --14 5
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --15 5
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --16 5
	{p1={x=80, y=5, z=-5}, p2={x=130, y=20, z=5}}, --17 5
	{p1={x=69, y=5, z=-5}, p2={x=130, y=32, z=5}}, --18 6
	{p1={x=69, y=5, z=-5}, p2={x=130, y=32, z=5}}, --19 7
	{p1={x=10, y=-60, z=-5}, p2={x=130, y=32, z=5}}, --20 8
	{p1={x=10, y=-60, z=-5}, p2={x=130, y=32, z=5}}, --21 9
	{p1={x=10, y=-60, z=-5}, p2={x=130, y=32, z=5}}, --22 10
}
		