lvim.leader = "space"

vim.cmd("noremap <up> <nop>")
vim.cmd("noremap <Down> <Nop>")
vim.cmd("noremap <Left> <Nop>")
vim.cmd("noremap <Right> <Nop>")
vim.cmd("inoremap <Up> <Nop>")
vim.cmd("inoremap <Down> <Nop>")
vim.cmd("inoremap <Left> <Nop>")
vim.cmd("inoremap <Right> <Nop>")
vim.cmd("vnoremap im aBoV")
vim.cmd("nnoremap J 5j")
vim.cmd("nnoremap K 5k")
vim.cmd('nnoremap "" vi"')
vim.cmd("vnoremap am aBjoV")

-- Show dependency versions
vim.keymap.set({ "n" }, "<LEADER>ns", require("package-info").show, { silent = true, noremap = true })

-- Hide dependency versions
vim.keymap.set({ "n" }, "<LEADER>nc", require("package-info").hide, { silent = true, noremap = true })

-- Toggle dependency versions
vim.keymap.set({ "n" }, "<LEADER>nt", require("package-info").toggle, { silent = true, noremap = true })

-- Update dependency on the line
vim.keymap.set({ "n" }, "<LEADER>nu", require("package-info").update, { silent = true, noremap = true })

-- Delete dependency on the line
vim.keymap.set({ "n" }, "<LEADER>nd", require("package-info").delete, { silent = true, noremap = true })

-- Install a new dependency
vim.keymap.set({ "n" }, "<LEADER>ni", require("package-info").install, { silent = true, noremap = true })

-- Install a different dependency version
vim.keymap.set({ "n" }, "<LEADER>np", require("package-info").change_version, { silent = true, noremap = true })
