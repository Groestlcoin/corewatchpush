class Config:
    #always use a BIP44 account key
    #keys will be derived at <xpub>/0/* and <xpub>/1/* (internal)
    #if you have an ypub or zpub, use Electrum-GRS' CLI to convert it to xpub ("convert_xkey(<ypub>, "standard")")
    bip44_account_xpubs=[["xpub661MyMwAqRbcEkSxvXEo7YjYynZAQ2MTEGgdKpUUXukRf33ymeCJasAS3g3QJoMmtCRPrJ1cvexQr7SF8W97dyjfR4miTksU9UtntYopk1B", "My Old Wallet", ["pkh()"]],
                         ["xpub68TU6zSxD4Jmf1wjF87utQsE7LoPnPjX8VEEAfpFLLWhduEMeNBsEohuqvpi6AP1RKpWPEamXCf3Q9uVpVDafuXnFPvVTkgr11jetqGq2ov", "My New Wallet", ["wpkh()"]],
                         ["xpub661MyMwAqRbcGAaqpmXCN8DVnH6oqd6L1VdczEmAeUmHaSMwNFPZCsDyEcBATWe2KTkBcxSqFANYx3hrJiRmd4NWAekoxvrJdBhY3ZBDj9Z", "My Other Wallet"]
                        ]

    # the range to derive addresses up to (for each script_type)
    xpub_range=1000

    # default script types to derive if no script type is given in bip44_account_xpubs
    script_types = ["pkh()", "wpkh()", "sh(wpkh())"]

    # groestlcoin cli location
    # requires Groestlcoin Core 2.18.2 (or newer)
    bitcoin_cli="/usr/bin/groestlcoin-cli"

    # groestlcoin
    bitcoin_cli_args=""

    # name of the wallet
    # WARNING: CoreWatchPush is not really multiwallet capable
    bitcoin_wallet_name="" #use empty string for default wallet

    # optional blockexplorer link
    blockexplorer = "https://esplora.groestlcoin.org/"

    # push channels (only telegram for now)
    notify_channels=["telegram"]
    #notify_channels=["telegram", "email"] #enable in case you want email and smtp

    # telegram KEY and chat-ID
    # google the internet how to create a bot, get the key as well as a chat-id
    notify_telegram_key="###"
    notify_telegram_chat_id="###"

    # email notification SMTP
    notify_email_receiver = "You <you@yourdomain.com>"
    notify_email_sender = "autosend <autosend@something.com>"
    notify_email_smtphost = "your.smtp.host"
    notify_email_smtpuser = "your_smtp_username"
    notify_email_smtppass = "your_smtp_password"
