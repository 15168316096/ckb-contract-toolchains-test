ckb-cli tx build-multisig-address \
  --require-first-n 0 \
  --threshold 1 \
  --sighash-address ckt1qyq829u0x32fchlfe5dqc4awh5q70h0eyj0qh8ngj4 \
  --sighash-address ckt1qyq283mcnqwpncwuccglkgfjmnd2cp662pjqykjl03

ckb-cli util address-info --address ckt1qpw9q60tppt7l3j7r09qcp7lxnp3vcanvgha8pmvsa3jplykxn32sqt2s9gjj38hlf00r3qvm08ltq6nkc95h6shwwklz

ckb-cli deploy gen-txs \
  --deployment-config ./deployment.toml \
  --migration-dir ./migrations \
  --from-address ckt1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsqt4z78ng4yutl5u6xsv27ht6q08mhujf8s2r0n40 \
  --info-file deploy-tx.json

ckb-cli deploy sign-txs --from-account ckt1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsqt4z78ng4yutl5u6xsv27ht6q08mhujf8s2r0n40 --info-file ./deploy-tx.json --add-signatures

ckb-cli deploy apply-txs --info-file ./deploy-tx.json --migration-dir ./migrations

ckb-cli deploy gen-txs \
  --deployment-config ./deployment.toml \
  --migration-dir ./migrations \
  --from-address ckt1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsqt4z78ng4yutl5u6xsv27ht6q08mhujf8s2r0n40 \
  --info-file update-tx.json
ckb-cli deploy sign-txs --from-account ckt1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsqt4z78ng4yutl5u6xsv27ht6q08mhujf8s2r0n40 --info-file ./update-tx.json --add-signatures

ckb-cli deploy apply-txs --info-file ./update-tx.json --migration-dir ./migrations
