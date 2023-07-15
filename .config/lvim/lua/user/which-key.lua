local kind = require("user.kind")
local wk = lvim.builtin.which_key

wk.mappings["p"] = {
	name = "last Session",
	s = { "<cmd>lua require('persistence').load()<cr>", kind.icons.clock .. " Reload last session for dir" },
	l = { "<cmd>lua require('persistence').load({ last = true })<cr>", kind.icons.clock .. " Restore last session" },
	Q = { "<cmd>lua require('persistence').stop()<cr>", kind.icons.exit .. " Quit without saving session" },
}

wk.mappings["r"] = {
	name = "code run",
	r = { "<cmd>RunCode<cr>", "Run Code" },
	f = { "<cmd>RunFiles<cr>", "Run File" },
	c = { "<cmd>RunClose<cr>", "Run Close" },
}
