lvim.plugins = {
	{
		"barrett-ruth/live-server.nvim",
		build = "yarn global add live-server",
		config = true,
	},
	{ "CRAG666/code_runner.nvim", config = true },
	{
		"microsoft/vscode-js-debug",
		opt = true,
		run = "npm install --legacy-peer-deps && npx gulp vsDebugServerBundle && mv dist out",
	},
	{
		"iamcco/markdown-preview.nvim",
		run = function()
			vim.fn["mkdp#util#install"]()
		end,
	},
	{
		"andrewferrier/wrapping.nvim",
		config = function()
			require("wrapping").setup()
		end,
	},
	{
		"stevearc/dressing.nvim",
		opts = {},
	},
	{ "nvimdev/hlsearch.nvim" },
	{
		"kylechui/nvim-surround",
		tag = "*", -- Use for stability; omit to use `main` branch for the latest features
		config = function()
			require("nvim-surround").setup({
				-- Configuration here, or leave empty to use defaults
			})
		end,
	},
	{
		"max397574/better-escape.nvim",
		config = function()
			require("better_escape").setup()
		end,
	},
	{
		"folke/trouble.nvim",
		cmd = "TroubleToggle",
	},
	{
		"ethanholz/nvim-lastplace",
	},
	{

		"nickeb96/fish.vim",
	},
	{ "uga-rosa/cmp-dictionary" },
	{ "hrsh7th/cmp-cmdline" },
	{ "f3fora/cmp-spell" },
	{ "hrsh7th/cmp-calc" },
	{ "norcalli/nvim-colorizer.lua" },
	{
		"rmagatti/goto-preview",
		config = function()
			require("goto-preview").setup({
				width = 120, -- Width of the floating window
				height = 25, -- Height of the floating window
				default_mappings = true, -- Bind default mappings
				debug = false, -- Print debug information
				opacity = nil, -- 0-100 opacity level of the floating window where 100 is fully transparent.
				post_open_hook = nil, -- A function taking two arguments, a buffer and a window to be ran as a hook.
			})
		end,
	},
	{
		"windwp/nvim-ts-autotag",
		config = function()
			require("nvim-ts-autotag").setup()
		end,
	},
	{
		"nvimdev/hlsearch.nvim",
		event = "BufRead",
		config = function()
			require("hlsearch").setup()
		end,
		{
			"folke/todo-comments.nvim",
			requires = "nvim-lua/plenary.nvim",
			config = function()
				require("todo-comments").setup({})
			end,
		},
	},
	{
		"folke/persistence.nvim",
		event = "BufReadPre", -- this will only start session saving when an actual file was opened
		module = "persistence",
		config = function()
			require("persistence").setup()
		end,
	},
}
