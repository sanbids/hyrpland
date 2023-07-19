reload("user.plugins")
reload("user.colorscheme")
reload("user.options")
reload("user.keymaps")
reload("user.lsp")
reload("user.kind")
reload("user.cmp")
reload("user.banners")
reload("user.which-key")
reload("user.code_runner")
reload("user.boole")

require("nvim-lightbulb").setup({
	autocmd = { enabled = true },
})
vim.opt.fillchars = { eob = " " }

require("hlsearch").setup({
	"*",
})
require("nvim-lastplace").setup({})

require("better_escape").setup({
	timeout = 300,
})

require("oil").setup()
