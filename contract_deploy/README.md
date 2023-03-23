<https://github.com/nervosnetwork/ckb-cli/wiki/Deploy-contracts>

```sh
$ ckb-cli deploy init-config --deployment-config deployment.toml
$ ckb-cli deploy gen-txs \
    --deployment-config ./deployment.toml \
    --migration-dir ./migrations \
    --from-address ckt1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsqt4z78ng4yutl5u6xsv27ht6q08mhujf8s2r0n40 \
    --sign-now \
    --info-file info.json
$ ckb-cli deploy sign-txs \
    --from-account ckt1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsqt4z78ng4yutl5u6xsv27ht6q08mhujf8s2r0n40 \
    --add-signatures \
    --info-file info.json
$ ckb-cli deploy apply-txs --migration-dir ./migrations --info-file info.json
```
