set -ex

lockarg1=0x75178f34549c5fe9cd1a0c57aebd01e7ddf9249e
lockarg2=0xa3c778981c19e1dcc611fb2132dcdaac075a5064

init_account() {
    rm -f ~/.ckb-cli/keystore/*
    echo 0000000000000000000000000000000000000000000000000000000000000001 > /tmp/foo
    ckb-cli account import --privkey-path /tmp/foo
    echo 0000000000000000000000000000000000000000000000000000000000000002 > /tmp/foo
    ckb-cli account import --privkey-path /tmp/foo
}

init_node() {
    cd /home/ubuntu/app/ckb
    rm -rf data specs ckb-miner.toml ckb.toml default.db-options
    ckb init --chain dev --ba-arg $lockarg1 --ba-message 0xabcd
    pmname=ckbr pm c ./ckb run
    sleep 4
    pmname=ckbm pm c ./ckb miner
    ckb-cli wallet get-capacity --lock-arg $lockarg1
}
