export Bin

ci:
	echo $(Bin)
	RUST_LOG=debug ckb-debugger  --cell-index 0 --cell-type input --script-group-type type --bin data/scripts/$(Bin)

install:
	cargo install --git https://github.com/nervosnetwork/ckb-standalone-debugger ckb-debugger

