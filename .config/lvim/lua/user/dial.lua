local augend = require("dial.augend")
require("dial.config").augends:register_group({
	default = {
		augend.integer.alias.decimal,
		augend.integer.alias.hex,
		augend.date.alias["%Y/%m/%d"],
	},
	typescript = {
		augend.integer.alias.decimal,
		augend.integer.alias.hex,
		augend.constant.new({ elements = { "let", "const" } }),
	},
	visual = {
		augend.integer.alias.decimal,
		augend.integer.alias.hex,
		augend.date.alias["%Y/%m/%d"],
		augend.constant.alias.alpha,
		augend.constant.alias.Alpha,
	},
})

vim.keymap.set("v", "<C-a>", require("dial.map").inc_visual("visual"), { noremap = true })
vim.keymap.set("v", "<C-x>", require("dial.map").dec_visual("visual"), { noremap = true })
