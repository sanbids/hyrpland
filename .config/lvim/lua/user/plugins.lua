lvim.plugins = {
  {
    "Pocco81/true-zen.nvim",
    config = function()
      require("true-zen").setup({
        -- your config goes here
        -- or just leave it empty :)
      })
    end,
  },
  {
    "folke/zen-mode.nvim",
    lazy = {
      -- your configuration comes here
      -- or leave it empty to use the default settings
      -- refer to the configuration section below
    },
  },
  {
    "stevearc/oil.nvim",
    lazy = {},
    -- lazyional dependencies
    dependencies = { "nvim-tree/nvim-web-devicons" },
  },
  { "kosayoda/nvim-lightbulb" },
  -- {
  -- 	"stevearc/dressing.nvim",
  -- 	lazy = {},
  -- },
  {
    "wintermute-cell/gitignore.nvim",
    dependencies = {
      "nvim-telescope/telescope.nvim",
    },
  },
  {
    "folke/flash.nvim",
    event = "VeryLazy",
    ---@type Flash.Config
    lazy = {},
    -- stylua: ignore
    keys = {
      { "s", mode = { "n", "x", "o" }, function() require("flash").jump() end,       desc = "Flash" },
      { "S", mode = { "n", "o", "x" }, function() require("flash").treesitter() end, desc = "Flash Treesitter" },
      { "r", mode = "o",               function() require("flash").remote() end,     desc = "Remote Flash" },
      {
        "R",
        mode = { "o", "x" },
        function() require("flash").treesitter_search() end,
        desc =
        "Treesitter Search"
      },
      {
        "<c-s>",
        mode = { "c" },
        function() require("flash").toggle() end,
        desc =
        "Toggle Flash Search"
      },
    },
  },

  { "nat-418/boole.nvim" },
  { "monaqa/dial.nvim" },
  { "kdheepak/cmp-latex-symbols" },
  { "uga-rosa/ccc.nvim" },
  { "bluz71/vim-nightfly-colors", name = "nightfly",   lazy = false,   priority = 1000 },
  { "rebelot/kanagawa.nvim" },
  { "EdenEast/nightfox.nvim" },
  { "catppuccin/nvim",            name = "catppuccin", priority = 1000 },
  { "rose-pine/neovim",           name = "rose-pine" },
  {
    "folke/tokyonight.nvim",
    -- lazy = false,
    priority = 1000,
    lazy = {},
  },
  { "kevinhwang91/nvim-ufo", dependencies = "kevinhwang91/promise-async" },
  { "nvim-pack/nvim-spectre" },
  {
    "barrett-ruth/live-server.nvim",
    build = "yarn global add live-server",
    config = true,
  },
  { "CRAG666/code_runner.nvim", config = true },
  {
    "microsoft/vscode-js-debug",
    lazy = true,
    build = "npm install --legacy-peer-deps && npx gulp vsDebugServerBundle && mv dist out",
  },
  {
    "iamcco/markdown-preview.nvim",
    build = function()
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
    version = "*", -- Use for stability; omit to use `main` branch for the latest features
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
        width = 120,             -- Width of the floating window
        height = 25,             -- Height of the floating window
        default_mappings = true, -- Bind default mappings
        debug = false,           -- Print debug information
        opacity = nil,           -- 0-100 opacity level of the floating window where 100 is fully transparent.
        post_open_hook = nil,    -- A function taking two arguments, a buffer and a window to be ran as a hook.
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
      dependencies = "nvim-lua/plenary.nvim",
      config = function()
        require("todo-comments").setup({})
      end,
    },
  },
  {
    "folke/persistence.nvim",
    event = "BufReadPre", -- this will only start session saving when an actual file was opened
    lazy = true,
    config = function()
      require("persistence").setup()
    end,
  },
}
