lvim.builtin.treesitter.auto_install = true
lvim.builtin.treesitter.ensure_installed = { "comment", "markdown_inline", "regex" }
lvim.lsp.installer.setup.automatic_servers_installation = true

local formatters = require("lvim.lsp.null-ls.formatters")
formatters.setup({
	{ command = "stylua", filetypes = { "lua" } },
	{
		command = "prettierd",
		filetypes = {
			"javascript",
			"javascriptreact",
			"typescript",
			"typescriptreact",
			"vue",
			"css",
			"scss",
			"less",
			"html",
			"yaml",
			"markdown",
			"markdown.mdx",
			"graphql",
			"handlebars",
			"json",
		},
	},
})

local linters = require("lvim.lsp.null-ls.linters")
linters.setup({
	{
		command = "eslint_d",
		filetypes = { "javascript", "typescript", "typescriptreact", "json" },
	},
	{
		command = "shellcheck",
		args = { "--severity", "warning" },
		filetypes = { "bash", "zsh" },
	},
	-- { command = "flake8", filetypes = { "python" } },
})
