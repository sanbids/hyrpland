reload("user.plugins")
reload("user.colorscheme")
reload("user.options")
reload("user.keymaps")
reload("user.lsp")
reload("user.dashboard")
reload("user.kind")
reload("user.cmp")
reload("user.banners")
reload("user.which-key")

require("hlsearch").setup({
	"*",
})
require("nvim-lastplace").setup({})

require("dressing").setup({})

