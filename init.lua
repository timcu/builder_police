--[[
Copyright (c) 2018 Triptera Pty Ltd

This minetest mod "builder_police", including its tasks and the associated 
pycharm-edu course, requires permission from Triptera Pty Ltd to use.

Permission is hereby granted, to any person at a CoderDojo session in 2018
to use the Software, including the right to copy, and/or distribute,
copies of the Software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

=========================================================================
https://github.com/timcu/builder_police
]]

local mod_storage = minetest.get_mod_storage()
local tbl_storage
local mod_this = minetest.get_current_modname() -- builder_police
local mod_irc_builder = 'irc_builder'

local function read_key(key) 
	return tbl_storage.fields[mod_this.."_"..key]
end

local function write_key(key, data) 
	tbl_storage.fields[mod_this.."_"..key] = data
end

local function write_storage()
	mod_storage:from_table(tbl_storage)
end

local assign_player_z = function(player_name)
	local str_player_names = read_key('player_names')
	local player_names = {}
	local found = false
	if str_player_names then
		--print("str_player_names = "..str_player_names)
		for name in str_player_names:gmatch("%S+") do
			--print("Checking name "..name)
			if name == player_name then
				found = true
			end
		end
	else
		print("str_player_names is nil")
	end
	if not found then
		if str_player_names then
			str_player_names = str_player_names.." "..player_name
		else
			str_player_names = player_name
		end
		write_key('player_names', str_player_names)
		write_storage()
		--print("written player_names "..str_player_names)
	end
	--print('player_names = '..str_player_names)
	local key = player_name..'_build_z'
	if tbl_storage.fields[key] then
		--print(key.." already "..tbl_storage.fields[key])
	else
		local next_z = tonumber(read_key('next_z'))
		local delta_z = tonumber(read_key('delta_z'))
		tbl_storage.fields[key]=next_z
		write_key('next_z',next_z + delta_z)
		write_storage()
		--print(key.." assigned "..next_z)
	end
end

local get_ground_level = function(x, z)
	return irc_builder.get_ground_level(x, z)
end  

builder_police = {
	version="0.0.5",
}
builder_police.get_player_z = function(player_name)
	local key = player_name..'_build_z'
	local z = tonumber(tbl_storage.fields[key])
	-- print("Ground level at 100," .. z .. " = "..get_ground_level(100, z))	
	return z
end

builder_police.get_delta_z = function()
	return tonumber(read_key('delta_z'))
end

local get_player_task = function(player_name)
	local key = player_name..'_task'
	return tonumber(tbl_storage.fields[key])
end

local set_player_task = function(player_name, task)
	--print(player_name..' assigned task '..task)
	minetest.chat_send_all(player_name..' assigned task '..task)
	local key = player_name..'_task'
	tbl_storage.fields[key] = task
	write_storage()
	print(player_name.." has been assigned task "..task)
end

local get_player_jail_free_task = function(player_name)
	local key = player_name..'_jail_free_task'
	local task = tonumber(tbl_storage.fields[key])
	return task and tonumber(task) or 0
end

local set_player_jail_free_task = function(player_name, task)
	--print(player_name..' assigned task '..task)
	local key = player_name..'_jail_free_task'
	tbl_storage.fields[key] = task
	write_storage()
end

local get_jail_free_task = function()
	local task = tonumber(read_key('jail_free_task'))
	return task and tonumber(task) or 0
end

local get_task_privileges = function()
	local task_privileges = read_key('task_privileges')
	if not task_privileges then
		task_privileges = '- - - - fly - fast - noclip'
		write_key('task_privileges', task_privileges)
	end
	return task_privileges
end

local get_task_privilege = function(task)
	local task_privileges = get_task_privileges()
	local priv
	local count = 1
	for p in task_privileges:gmatch("(%S+)") do
		if count == task then
			priv = p
		end
		count = count + 1
	end
	return priv
end

local function read_storage()
	tbl_storage = mod_storage:to_table()
	if not tbl_storage then 
		print('tbl_storage nil so initialising')
		tbl_storage = {} 
	else
		--print('tbl_storage not nil. start_x=')
		--print(tonumber(read_key('start_x')))
		--print(minetest.serialize(tbl_storage))
	end
	if not tonumber(read_key('start_x')) then write_key('start_x',100) end
	if not tonumber(read_key('start_y')) then write_key('start_y',10)  end
	if not tonumber(read_key('start_z')) then write_key('start_z',10)  end
	if not tonumber(read_key('delta_z')) then write_key('delta_z',10)  end
	if not tonumber(read_key('next_z'))  then write_key('next_z',tonumber(read_key('start_z'))) end
	for _,player in ipairs(minetest.get_connected_players()) do
		assign_player_z(player:get_player_name())
	end
end

-- run read_storage early on
read_storage()

minetest.register_privilege("police", {
    description = "Can use builder_police commands to control players",
    give_to_singleplayer = true
})

minetest.register_on_shutdown(function()
	--print('on_shutdown')
	write_storage()
end)

dofile(minetest.get_modpath(mod_irc_builder) .. "/chatcmdbuilder.lua")

minetest.register_chatcommand("get_player_z", {
	params = "<player_name>",
	description = "Get builder_police z value for player so they know where they can build",
	privs = {},
	func = function( name , player_name)
		if player_name then
			return true, ""..builder_police.get_player_z(player_name)
		else
			return true, ""..builder_police.get_player_z(name)
		end
	end,
})

minetest.register_chatcommand("set_jail_free_task", {
	params = "<task_number>",
	description = "Sets the number of the task which must be completed to get out of jail",
	privs = {police = true},
	func = function(name, task)
		local task_number = tonumber(task)
		if task_number then
			write_key('jail_free_task', task_number)
			return true, "jail_free_task is now "..read_key('jail_free_task')
		else
			return false, "You must provide a numerical task number"
		end
	end,
})

minetest.register_chatcommand("get_player_task", {
	params = "<player_name>",
	description = "Gets the number of the first task which has not yet been completed by player",
	privs = {},
	func = function(name, player_name)
		return true, ""..get_player_task(player_name)
	end,
})

minetest.register_chatcommand("set_player_task", {
	params = "<player_name> <task_number>",
	description = "Sets the number of the first task which has not yet been completed by player",
	privs = {police = true},
	func = function(name, param)
		local player_name, task = param:match("(%S+) (%d+)")
		local task_number = tonumber(task)
		if task_number then
			set_player_task(player_name, task_number)
			return true, player_name.."'s next task is now "..get_player_task(player_name)
		else
			return false, "You must provide a player_name and numerical task_number"
		end
	end,
})

builder_police.pos_build = function(player_name)
	return {x=tonumber(read_key('start_x')), y = tonumber(read_key('start_y')), z = builder_police.get_player_z(player_name)}
end

dofile(minetest.get_modpath(mod_this) .. "/set1/tasks.lua")

minetest.register_on_joinplayer(function(player)
	assign_player_z(player:get_player_name())
	player:setpos({x=102,y=9.5,z=builder_police.get_player_z(player:get_player_name())})
	--following line only required if using physics to keep players in jail
	--player:set_physics_override({jump=1, speed=1, gravity=1})
end)

minetest.register_on_newplayer(function(player)
	-- new players given irc_builder privilege
	local privs = minetest.get_player_privs(player:get_player_name())
	privs.irc_builder = true
	minetest.set_player_privs(player:get_player_name(), privs)
end)

local pvp = minetest.settings:get("enable_pvp")
if pvp then
	-- print("registering on punchplayer")
	minetest.register_on_punchplayer(function(hittee, hitter, time_from_last_punch, tool_capabilities, dir, damage)
		local player_name = hitter:get_player_name()
		local task = get_player_task(player_name)
		if not task or task < 1 then task = 1 end
		hitter:set_physics_override({jump=0, speed=0, gravity=0})
		-- player has to complete current task to get out of jail
		set_player_jail_free_task(player_name, task)
		hitter:setpos({x=102,y=9.5,z=builder_police.get_player_z(player_name)})
		minetest.chat_send_all(player_name..' has been jailed and immobilised for one task for hitting '..hittee:get_player_name())
	end)
end

local timer = 0
minetest.register_globalstep(function(dtime)
	timer = timer + dtime
	if timer >= 5 then
		timer = 0
		local str_player_names = read_key('player_names')
		local jail_free_task = tonumber(read_key('jail_free_task'))
		if not jail_free_task then jail_free_task = 0 end
		local players = {}
		for _,player in ipairs(minetest.get_connected_players()) do
			players[player:get_player_name()]=player
		end
		--print("Jail free task ")
		--print(jail_free_task)
		if str_player_names then
			for player_name in str_player_names:gmatch("%S+") do
				local z = builder_police.get_player_z(player_name)
				local task = get_player_task(player_name)
				local player_jail_free_task = get_player_jail_free_task(player_name)
				if not task or task < 1 then
					task = 1
					set_player_task(player_name, task)
					builder_police.tasks[task](player_name) 
				end
				while builder_police.tests[task](player_name) and task < #builder_police.tests do
					if player_name and task then
						-- player has completed their next task
						minetest.chat_send_all(player_name.." has completed task "..task)
						-- check what privileges player gets for completing task and grant them
						local privs = minetest.get_player_privs(player_name)
						local task_privileges = get_task_privileges()
						local count = 1
						for p in task_privileges:gmatch("(%S+)") do
							if count <= task and p and p ~= "-" then
								privs[p] = true
							end
							count = count + 1
						end
						minetest.set_player_privs(player_name, privs)
					end		
					task = task + 1
					set_player_task(player_name, task)
					builder_police.tasks[task](player_name) 
				end
				-- test current players to see which ones need to be in jail
				local player = players[player_name]
				if player then
					if (task <= jail_free_task) or (player_jail_free_task and task <= player_jail_free_task) then
						local p1 = builder_police.jails[task].p1
						local p2 = builder_police.jails[task].p2
						local p = player:getpos()
						if p.x < p1.x or p.x > p2.x or p.y < p1.y or p.y > p2.y or p.z < p1.z + z or p.z > p2.z + z then
							--player:set_physics_override({jump=0, speed=0, gravity=0})
							--print(minetest.serialize(p)..minetest.serialize(p1)..minetest.serialize(p2))
							player:setpos({x=102,y=9.5,z=z})
						end
					end
					-- check players who were in jail for punching other players and remobilise them if they have completed next task
					if (player_jail_free_task and (task > player_jail_free_task or player_jail_free_task > #builder_police.tasks)) then
						set_player_jail_free_task(player_name, 0)
						player:set_physics_override({jump=1, speed=1, gravity=1})
					end
				end
			end
		end
	end
end) 
