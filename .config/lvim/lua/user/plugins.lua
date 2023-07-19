lvim.plugins = {
	{ "dundalek/lazy-lsp.nvim", requires = { "neovim/nvim-lspconfig" } },
	{
		"vuki656/package-info.nvim",
		requires = "MunifTanjim/nui.nvim",
	},
	{
		"stevearc/oil.nvim",
		opts = {},
		-- Optional dependencies
		dependencies = { "nvim-tree/nvim-web-devicons" },
	},
	{
		"mrbjarksen/neo-tree-diagnostics.nvim",
		requires = "nvim-neo-tree/neo-tree.nvim",
		module = "neo-tree.sources.diagnostics", -- if wanting to lazyload
	},
	{
		"neovim/nvim-lspconfig",
		dependencies = {
			{
				"SmiteshP/nvim-navbuddy",
				dependencies = {
					"SmiteshP/nvim-navic",
					"MunifTanjim/nui.nvim",
				},
				opts = { lsp = { auto_attach = true } },
			},
		},
		-- your lsp config or other stuff
	},
	{ "kosayoda/nvim-lightbulb" },
	{
		"ray-x/lsp_signature.nvim",
	},
	-- {
	-- 	"stevearc/dressing.nvim",
	-- 	opts = {},
	-- },
	{
		"wintermute-cell/gitignore.nvim",
		requires = {
			"nvim-telescope/telescope.nvim",
		},
	},
	{
		"folke/flash.nvim",
		event = "VeryLazy",
		---@type Flash.Config
		opts = {},
  -- stylua: ignore
  keys = {
    { "s", mode = { "n", "x", "o" }, function() require("flash").jump() end, desc = "Flash" },
    { "S", mode = { "n", "o", "x" }, function() require("flash").treesitter() end, desc = "Flash Treesitter" },
    { "r", mode = "o", function() require("flash").remote() end, desc = "Remote Flash" },
    { "R", mode = { "o", "x" }, function() require("flash").treesitter_search() end, desc = "Treesitter Search" },
    { "<c-s>", mode = { "c" }, function() require("flash").toggle() end, desc = "Toggle Flash Search" },
  },
	},

	{ "nat-418/boole.nvim" },
	{ "monaqa/dial.nvim" },
	{ "kdheepak/cmp-latex-symbols" },
	{ "uga-rosa/ccc.nvim" },
	{ "bluz71/vim-nightfly-colors", name = "nightfly", lazy = false, priority = 1000 },
	{ "rebelot/kanagawa.nvim" },
	{ "EdenEast/nightfox.nvim" },
	{ "catppuccin/nvim", name = "catppuccin", priority = 1000 },
	{ "rose-pine/neovim", name = "rose-pine" },
	{
		"folke/tokyonight.nvim",
		lazy = false,
		priority = 1000,
		opts = {},
	},
	{ "kevinhwang91/nvim-ufo", requires = "kevinhwang91/promise-async" },
	{ "nvim-pack/nvim-spectre" },
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
