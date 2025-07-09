"use strict";

const titleText = document.getElementById('titleText');
const startText = document.getElementById('startText');
const menu = document.getElementById('menu');
const start = document.getElementById('start');
const textMode = document.getElementById('textMode');
const wordMode = document.getElementById('wordMode');
const endress = document.getElementById('endress');
const home = document.getElementById('home');
const help = document.getElementById('help');
const play = document.getElementById('play');
const Q1 = document.getElementById('Q1');
const Q2 = document.getElementById('Q2');
const Q3 = document.getElementById('Q3');
const result = document.getElementById('result');
const resultLeft = document.getElementById('resultLeft');
const resultRight = document.getElementById('resultRight');
const resultWeakKey = document.getElementById('resultWeakKey');
const resultMissNumOfType = document.getElementById('resultMissNumOfType');
const resultNumOfType = document.getElementById('resultNumOfType');
const resultAccyracyRate = document.getElementById('resultAccyracyRate');
const resultTime = document.getElementById('resultTime');
const resultWPM = document.getElementById('resultWpm');
const resultScore = document.getElementById('resultScore');
const resultLebel = document.getElementById('resultLebel');
const history = document.getElementById('history');
const nameInput = document.getElementById('nameInput');

let username = '';
let startFlag = false;
startText.onclick = function () {
    startFlag = true;
    menu.classList.add("NoneClass");
    start.classList.remove("NoneClass");
    username = nameInput.value;
};

let ModeSectFlag = -1;
let endressFlag = false;
textMode.onclick = function () {
    if (ModeSectFlag === -1 || ModeSectFlag === 2) {
        ModeSectFlag = 1;
        textMode.style.border = 'solid yellow 5px';
        textMode.style.background = 'rgb(89, 158, 174)';
        wordMode.style.border = 'solid white 5px';
        wordMode.style.background = 'rgb(129, 232, 255)';
    }
}

wordMode.onclick = function () {
    if (ModeSectFlag === -1 || ModeSectFlag === 1) {
        ModeSectFlag = 2;
        wordMode.style.border = 'solid yellow 5px';
        wordMode.style.background = 'rgb(89, 158, 174)';
        textMode.style.border = 'solid white 5px';
        textMode.style.background = 'rgb(129, 232, 255)';
    }
}

endress.onclick = function () {
    if (endressFlag === false) {
        endressFlag = true;
        endress.style.border = 'solid yellow 5px';
        endress.style.background = 'rgb(147, 75, 75)';
    } else {
        endressFlag = false;
        endress.style.border = 'solid white 5px';
        endress.style.background = 'rgb(255, 133, 133)';
    }
}

let timeFlag = false;
home.onclick = function () {
    startFlag = false;
    start.classList.add("NoneClass");
    play.classList.add("NoneClass");
    menu.classList.remove("NoneClass");
    result.classList.add("NoneClass");
    resultLeft.classList.add("NoneClass");
    resultRight.classList.add("NoneClass");
    Q1.textContent = ``;
    Q2.textContent = ``;
    Q3.textContent = ``;
    txtIndex = 0;
    newSpan.textContent = '';
    i = 1;
    textMode.style.border = 'solid white 5px';
    textMode.style.background = 'rgb(129, 232, 255)';
    wordMode.style.border = 'solid white 5px';
    wordMode.style.background = 'rgb(129, 232, 255)';
    ModeSectFlag = -1;
    missList = [];
    missCount = 0;
    typeCount = 0;
    miss = '';
    if (resultWeakKey.contains(p1)) {
        resultWeakKey.removeChild(p1);
    }
    if (resultNumOfType.contains(p2)) {
        resultNumOfType.removeChild(p2);
    }
    if (resultAccyracyRate.contains(p3)) {
        resultAccyracyRate.removeChild(p3);
    }
    if (resultMissNumOfType.contains(p4)) {
        resultMissNumOfType.removeChild(p4);
    }
    if (resultTime.contains(p5)) {
        resultTime.removeChild(p5);
    }
    if (resultWPM.contains(p6)) {
        resultWPM.removeChild(p6);
    }
    if (resultScore.contains(p7)) {
        resultScore.removeChild(p7);
    }
    if (resultLebel.contains(p8)) {
        resultLebel.removeChild(p8);
    }
    score = 0;
    // resultLeftのすべての子要素を削除
    while (resultLeft.firstChild) {
        resultLeft.removeChild(resultLeft.firstChild);
    }
    // divResultのすべての子要素を削除
    const divResults = [divResult1, divResult2, divResult3, divResult4, divResult5, divResult6, divResult7, divResult8, divResult9, divResult10];
    divResults.forEach(div => {
        while (div.firstChild) {
            div.removeChild(div.firstChild);
        }
    });

    let p = document.createElement('p');
    p.textContent = 'タイピング';
    resultLeft.appendChild(p);
    i = 0;

    if (timeFlag === true) {
        timeCount = 0;
        clearInterval(intarvald);
        timeFlag = false;
    }
}

let helpFlag = false;
help.onclick = function () {
    if (helpFlag === false) {
        helpFlag = true;
        const helpDiv = document.getElementById("helpDiv");
        helpDiv.style.display = "block";
    } else {
        helpDiv.style.display = "None";
        helpFlag = false;
    }
};

let historyFlag = false;
const historyP = document.createElement('p');
history.onclick = function () {
    if (historyFlag === false) {
        historyFlag = true;
        const historyDiv = document.getElementById("historyDiv");
        historyDiv.style.display = "block";

        // 既存の内容をクリア
        historyDiv.innerHTML = '';

        // ローカルストレージからすべてのユーザーネームとスコアを取得
        for (let i = 0; i < localStorage.length; i++) {
            const key = localStorage.key(i);
            const value = localStorage.getItem(key);

            // スコアを数値に変換
            const score = parseInt(value, 10);

            // レベルを計算
            let level = '';
            if (score === 'NaN') {
                level = 'Error';
            }
            else if (score < 21) {
                level = 'E-';
            } else if (score < 38) {
                level = 'E';
            } else if (score < 55) {
                level = 'E+';
            } else if (score < 72) {
                level = 'D-';
            } else if (score < 89) {
                level = 'D';
            } else if (score < 106) {
                level = 'D+';
            } else if (score < 123) {
                level = 'C-';
            } else if (score < 140) {
                level = 'C';
            } else if (score < 157) {
                level = 'C+';
            } else if (score < 174) {
                level = 'B-';
            } else if (score < 191) {
                level = 'B';
            } else if (score < 208) {
                level = 'B+';
            } else if (score < 225) {
                level = 'A-';
            } else if (score < 242) {
                level = 'A';
            } else if (score < 259) {
                level = 'A+';
            } else if (score < 276) {
                level = 'S';
            } else {
                level = 'Good!';
            }

            // ユーザーネーム、スコア、レベルを表示
            const historyP = document.createElement('p');
            historyP.textContent = `${key}…スコア: ${score}, 　レベル: ${level}`;
            historyDiv.appendChild(historyP);
        }
    } else {
        const historyDiv = document.getElementById("historyDiv");
        historyDiv.style.display = "none";
        historyFlag = false;
    }
};

let wordList = [
    'プログラム', 'コンピューター', 'インターネット', 'データベース', 'サーバー',
    'クラウド', 'セキュリティ', 'ネットワーク', 'アルゴリズム', 'コード',
    'ソフトウェア', 'ハードウェア', 'バグ', 'アプリケーション', 'ファイル',
    'システム', 'プロトコル', 'デバッグ', 'デプロイ', 'エンジニア',
    'デベロッパー', 'フロントエンド', 'バックエンド', 'フルスタック', 'ビット',
    'バイト', 'オペレーティングシステム', 'メモリ', 'ストレージ', 'ユーザーインターフェース',
    'ウェブサイト', 'ブラウザ', 'スタイルシート', 'スクリーンリーダー', 'サイバー攻撃',
    'データ科学', '機械学習', '人工知能', '大規模データ', 'クラスタリング',
    'データ解析', 'ニューラルネットワーク', '深層学習', 'サイバーセキュリティ', '暗号化',
    'ディスク', 'ドライブ', 'キーボード', 'マウス', 'モニター',
    'プリンター', 'スキャナー', 'カメラ', 'ルーター', 'スイッチ',
    'ファイアウォール', '仮想プライベートネットワーク', 'パケット', 'プロキシ', '通信プロトコル',
    'データセンター', 'ホスティング', 'ドメイン', '名前解決システム', 'アドレス',
    'ログファイル', 'デフォルト設定', '構成ファイル', 'インストール', '更新プログラム',
    'バージョン管理', 'リリース', '保守', 'サポート', 'バックアップ',
    'リカバリー', 'エクスポート', 'インポート', 'シミュレーション', 'モデリング',
    'パフォーマンス', 'ロギング', 'トランザクション', 'セッション', 'キャッシュ',
    '問い合わせ言語', 'コンパイル', 'インタープリター', 'ライブラリ', 'フレームワーク',
    'パッケージ', 'モジュール', 'インスタンス', 'オブジェクト指向', 'クラス',
    'メソッド', 'プロパティ', 'コンストラクター', 'デストラクター', '多態性',
    'インターフェース', '抽象化', 'カプセル化', 'フィールド', 'エラーハンドリング'
];

let wordList3 = [
    'puroguramu', 'konpy-ta-', 'inta-netto', 'de-tabe-su', 'sa-ba-',
    'kuraudo', 'sekyurithi', 'nettowa-ku', 'arugorizumu', 'ko-do',
    'sofutowea', 'ha-dowea', 'bagu', 'apurike-syon', 'fairu',
    'sisutemu', 'purotokoru', 'debaggu', 'depuroi', 'enjinia',
    'deberoppa-', 'furontoendo', 'bakkuendo', 'furusutakku', 'bitto',
    'baito', 'opere-thingusisutemu', 'memori', 'sutore-zi', 'yu-za-inta-fe-su',
    'webusaito', 'burauza', 'sutairusi-to', 'sukuri-nri-da-', 'saiba-kougeki',
    'de-takagaku', 'kikaigakusyuu', 'jinkoutinou', 'daikibode-ta', 'kurasutaringu',
    'de-takaiseki', 'nyu-ralunettowa-ku', 'sinsougakusyuu', 'saiba-sekyurithi', 'angouka',
    'dhisuku', 'doraibu', 'ki-bo-do', 'mausu', 'monita-',
    'purinta-', 'sukyana-', 'kamera', 'ru-ta-', 'suitti',
    'faiawho-ru', 'kasoupuraibe-tonettowa-ku', 'paketto', 'purokisi', 'tuusinpurotokoru',
    'de-tasenta-', 'hosuthingu', 'domein', 'namaekaiketusisutemu', 'adoresu',
    'rogufairu', 'deforutosettei', 'kouseifairu', 'insuto-ru', 'kousinpuroguramu',
    'ba-jonkanri', 'riri-su', 'hosyu', 'sapo-to', 'bakkuappu',
    'rikabari-', 'ekusupo-to', 'inpo-to', 'simyure-syon', 'moderingu',
    'pafo-mansu', 'rogingu', 'toranzakusyon', 'sessyon', 'kyassyu',
    'toiawasegengo', 'konpairu', 'inta-purita-', 'raiburari', 'fure-muwa-ku',
    'pakke-ji', 'mozyu-ru', 'insutansu', 'obujyekutosikou', 'kurasu',
    'mesoddo', 'puropathi', 'konsutorakuta-', 'desutorakuta-', 'tataisei',
    'inta-fe-su', 'tyuusyouka', 'kapuseruka', 'fi-rudo', 'era-handoringu'
];

let textList = [
    'プログラミングは創造的な作業です',
    'インターネットは情報の宝庫です',
    'データベースは効率的な情報管理を可能にします',
    'サーバーはウェブサイトを支えています',
    'クラウドサービスは便利です',
    'セキュリティは大切です',
    'ネットワークは世界をつなぎます',
    'アルゴリズムは問題解決の鍵です',
    'コードを書くのは楽しいです',
    'ソフトウェアは日常生活を支えています',
    'ハードウェアはソフトウェアを動かします',
    'バグを見つけるのは重要です',
    'アプリケーションは多様な機能を持っています',
    'ファイルはデジタルデータを保持します',
    'システムの安定性は重要です',
    'プロトコルは通信のルールです',
    'デバッグはプログラミングの一部です',
    'デプロイはソフトウェアの公開です',
    'エンジニアは問題解決者です',
    'デベロッパーは新しいアプリケーションを作ります',
    'フロントエンドはユーザーの目に見える部分です',
    'バックエンドはシステムの裏側です',
    'フルスタックは幅広い知識を持っています',
    'ビットは情報の最小単位です',
    'バイトは8ビットで構成されます',
    'オペレーティングシステムはコンピューターを動かします',
    'メモリはデータを一時的に保存します',
    'ストレージはデータを永続的に保存します',
    'ユーザーインターフェースは使いやすさを決定します',
    'ウェブサイトは情報の発信源です',
    'ブラウザはウェブサイトを表示します',
    'スタイルシートはウェブサイトの見た目を決めます',
    'スクリーンリーダーは視覚障害者を支援します',
    'サイバー攻撃は深刻な脅威です',
    'データ科学は新しい知識を発見します',
    '機械学習はデータから学びます',
    '人工知能は未来の技術です',
    '大規模データは分析を可能にします',
    'クラスタリングはデータをグループ化します',
    'データ解析は意思決定を支援します',
    'ニューラルネットワークは脳を模倣します',
    '深層学習は高度な学習方法です',
    'サイバーセキュリティはデータを保護します',
    '暗号化は情報を安全にします',
    'ディスクはデータを保存します',
    'ドライブはデータを読み書きします',
    'キーボードは入力デバイスです',
    'マウスはポインティングデバイスです',
    'モニターは出力デバイスです',
    'プリンターはデジタルデータを印刷します',
    'スキャナーは紙の書類をデジタル化します'
];

let textList2 = [
    'ぷろぐらみんぐはそうぞうてきなさぎょうです',
    'いんたーねっとはじょうほうのほうこです',
    'でーたべーすはこうりつてきなじょうほうかんりをかのうにします',
    'さーばーはうぇぶさいとをささえています',
    'くらうどさーびすはべんりです',
    'せきゅりてぃはたいせつです',
    'ねっとわーくはせかいをつなぎます',
    'あるごりずむはもんだいかいけつのかぎです',
    'こーどをかくのはたのしいです',
    'そふとうぇあはにちじょうせいかつをささえています',
    'はーどうぇあはそふとうぇあをうごかします',
    'ばぐをみつけるのはじゅうようです',
    'あぷりけーしょんはたようなきのうをもっています',
    'ふぁいるはでじたるでーたをほじします',
    'しすてむのあんていせいはじゅうようです',
    'ぷろとこるはつうしんのるーるです',
    'でばっぐはぷろぐらみんぐのいちぶです',
    'でぷろいはそふとうぇあのこうかいです',
    'えんじにあはもんだいかいけつしゃです',
    'でべろっぱーはあたらしいあぷりけーしょんをつくります',
    'ふろんとえんどはゆーざーのめにみえるぶぶんです',
    'ばっくえんどはしすてむのうらがわです',
    'ふるすたっくははばひろいちしきをもっています',
    'びっとはじょうほうのさいしょうたんいです',
    'ばいとは8びっとでこうせいされます',
    'おぺれーてぃんぐしすてむはこんぴゅーたーをうごかします',
    'めもりはでーたをいちじてきにほぞんします',
    'すとれーじはでーたをえいぞくてきにほぞんします',
    'ゆーざーいんたーふぇーすはつかいやすさをけっていします',
    'うぇぶさいとはじょうほうのはっしんげんです',
    'ぶらうざはうぇぶさいとをひょうじします',
    'すたいるしーとはうぇぶさいとのみためをきめます',
    'すくりーんりーだーはしかくしょうがいしゃをしえんします',
    'さいばーこうげきはしんこくなきょういです',
    'でーたかがくはあたらしいちしきをはっけんします',
    'きかいがくしゅうはでーたからまなびます',
    'じんこうちのうはみらいのぎじゅつです',
    'だいきぼでーたはぶんせきをかのうにします',
    'くらすたりんぐはでーたをぐるーぷかします',
    'でーたかいせきはいしけっていをしえんします',
    'にゅーらるねっとわーくはのうをもほうします',
    'しんそうがくしゅうはこうどながくしゅうほうほうです',
    'さいばーせきゅりてぃはでーたをほごします',
    'あんごうかはじょうほうをあんぜんにします',
    'でぃすくはでーたをほぞんします',
    'どらいぶはでーたをよみかきします',
    'きーぼーどはにゅうりょくでばいすです',
    'まうすはぽいんてぃんぐでばいすです',
    'もにたーはしゅつりょくでばいすです',
    'ぷりんたーはでじたるでーたをいんさつします',
    'すきゃなーはかみのしょるいをでじたるかします'
];

let textList3 = [
    'puroguraminguhasouzoutekinasagyoudesu',
    'inta-nettohajouhounohoukodesu',
    'de-tabe-suhakouritutekinajouhoukanriwokanounisimasu',
    'sa-ba-hawebusaitowosasaeteimasu',
    'kuraudosa-bisuhabenridesu',
    'sekyurithihataisetudesu',
    'nettowa-kuhasekaiwotunagimasu',
    'arugorizumuhamondaikaiketunokagidesu',
    'ko-dowokakunohatanosiidesu',
    'sofutoweahanichijouseikatuwosasaeteimasu',
    'ha-doweahasofutoweawougokasimasu',
    'baguwomitukerunohajuuyoudesu',
    'apurike-syonhatayounakinouwomotteimasu',
    'fairuhadejitarude-tawohojisimasu',
    'sisutemunoanteiseihajuuyoudesu',
    'purotokoruhatuusinnoru-rudesu',
    'debagguhapuroguramingunoichibudesu',
    'depuroihasofutoweanokoukaidesu',
    'enjiniahamondaikaiketusyadesu',
    'deberoppa-haatarasiiapurike-syonwotukurimasu',
    'furontoendohayu-za-nomenimierububundesu',
    'bakkuendohasisutemunouragawadesu',
    'furusutakkuhahabahiroichisikiwomotteimasu',
    'bittohajouhounosaisyoutanidesu',
    'baitoha8bittodekouseisaremasu',
    'opere-thingusisutemuhakonpyu-tawougokasimasu',
    'memorihade-tawoichijitekinihozonsimasu',
    'sutore-jihade-tawoeizokutekinihozonsimasu',
    'yu-za-inta-fe-suhatukaiyasusawoketteisimasu',
    'webusaitohajouhounohassingendesu',
    'burauzahawebusaitowohyoujisimasu',
    'sutairusi-tohawebusaitonomitamewokimemasu',
    'sukuri-nri-da-hasikakusyougaisyawosiensimasu',
    'saiba-kougekihasinkokunakyouidesu',
    'de-takagakuhaatarasiichisikiwohakkensimasu',
    'kikaigakusyuuhade-takaramanabimasu',
    'jinkouchinouhamirainogijutudesu',
    'daikibode-tahabunsekiwokanounisimasu',
    'kurasutaringuhade-tawoguru-pukasimasu',
    'de-takaiseikihaisiketteiwosiensimasu',
    'nyu-ralunettowa-kuhanouwomohousimasu',
    'sinsougakusyuuhakoudonagakusyuuhouhoudesu',
    'saiba-sekyurithihade-tawohogosimasu',
    'angoukahajouhouwoanzennisimasu',
    'dhisukuhade-tawohozonsimasu',
    'doraibuhade-tawoyomikakisimasu',
    'ki-bo-dohanyuuryokudebaisudesu',
    'mausuhapointhingudebaisudesu',
    'monita-hasyuturyokudebaisudesu',
    'purinta-hadejitarude-tawoinsatusimasu',
    'sukyana-hakaminosyoruiwodejitarukasimasu'
];

let wordnums = [];
let textnums = [];
let timeCount = 0;
let intarvald;

document.addEventListener('keydown', function (event) {
    if (event.code === 'Space') {
        if (startFlag === true) {
            if (timeFlag === false) {
                timeFlag = true;
                intarvald = setInterval(function () {
                    timeCount += 1;
                }, 1000);

            }

            if (endressFlag === true) {
                wordnums = getRandomNumbers(0, 100, 100);
                textnums = getRandomNumbers(0, 50, 50);
            } else {
                wordnums = getRandomNumbers(0, 100, 10);
                textnums = getRandomNumbers(0, 50, 10);
            }

            if (ModeSectFlag === -1) {
                alert('モードを選択してください。')
            } else {
                startFlag = false;
                start.classList.add("NoneClass");
                play.classList.remove("NoneClass");
                let num = 3;
                Q3.textContent = `${num}`;
                const countdown = setInterval(function () {
                    num -= 1;
                    Q3.textContent = `${num}`;
                    if (num === 0) {
                        clearInterval(countdown);
                    }
                    if (num === 0) {
                        if (ModeSectFlag === 1) {
                            num = textnums[0]
                            Q1.textContent = `${textList[num]}`;
                            Q2.textContent = `${textList2[num]}`;
                            Q3.textContent = `${textList3[num]}`;
                        } else {
                            num = wordnums[0]
                            Q1.textContent = `${wordList[num]}`;
                            Q3.textContent = `${wordList3[num]}`;
                        }
                    }
                }, 1000);

            }
        }
    }
});

let score = 0;
let missList = [];
let missCount = 0;
let typeCount = 0;
let i = 0;
let txtIndex = 0;
let newSpan = document.createElement('span');
const divResult1 = document.createElement('div');
const divResult2 = document.createElement('div');
const divResult3 = document.createElement('div');
const divResult4 = document.createElement('div');
const divResult5 = document.createElement('div');
const divResult6 = document.createElement('div');
const divResult7 = document.createElement('div');
const divResult8 = document.createElement('div');
const divResult9 = document.createElement('div');
const divResult10 = document.createElement('div');
const p1 = document.createElement('p');
const p3 = document.createElement('p');
const p2 = document.createElement('p');
const p4 = document.createElement('p');
const p5 = document.createElement('p');
const p6 = document.createElement('p');
const p7 = document.createElement('p');
const p8 = document.createElement('p');

let miss = '';
document.addEventListener('keydown', function (event) {
    typeCount += 1;
    // 入力キーを取得
    let inputKey = event.key;

    // Q3のテキスト内容を取得
    let textContent = Q3.textContent;

    if (textContent[txtIndex] !== inputKey && ModeSectFlag === 2 || textContent[txtIndex] !== inputKey && ModeSectFlag === 1) {
        missCount += 1;

        if (inputKey === 'Enter') {
        } else if (inputKey === ' ') {
        } else {
            missList.push(inputKey);
        }
    }
    if (textContent[txtIndex] === inputKey) {

        // 新しいスパン要素を作成
        newSpan.textContent += inputKey;

        let txtLen = textContent.length;
        // 1文字目を削除した新しいテキスト内容を作成
        let newTextContent = textContent.slice(txtIndex + 1, txtLen);

        // 結果をQ3のテキスト内容に戻す
        Q3.textContent = newTextContent;

        // スパン要素をQ3の先頭に挿入
        Q3.insertBefore(newSpan, Q3.firstChild);

        txtIndex += 1;
        if (txtIndex === textContent.length) {
            if (i + 1 === 1) {
                const divP1 = document.createElement('p');
                const divP2 = document.createElement('p');
                divP1.textContent = `${i + 1}：`
                divP2.textContent = `${Q3.textContent}`;
                divResult1.appendChild(divP1);
                divResult1.appendChild(divP2);
                divResult1.classList.add("flexClass");
                resultLeft.appendChild(divResult1);
            } else if (i + 1 === 2) {
                const divP1 = document.createElement('p');
                const divP2 = document.createElement('p');
                divP1.textContent = `${i + 1}：`
                divP2.textContent = `${Q3.textContent}`;
                divResult2.appendChild(divP1);
                divResult2.appendChild(divP2);
                divResult2.classList.add("flexClass");
                resultLeft.appendChild(divResult2);
            } else if (i + 1 === 3) {
                const divP1 = document.createElement('p');
                const divP2 = document.createElement('p');
                divP1.textContent = `${i + 1}：`
                divP2.textContent = `${Q3.textContent}`;
                divResult3.appendChild(divP1);
                divResult3.appendChild(divP2);
                divResult3.classList.add("flexClass");
                resultLeft.appendChild(divResult3);
            } else if (i + 1 === 4) {
                const divP1 = document.createElement('p');
                const divP2 = document.createElement('p');
                divP1.textContent = `${i + 1}：`
                divP2.textContent = `${Q3.textContent}`;
                divResult4.appendChild(divP1);
                divResult4.appendChild(divP2);
                divResult4.classList.add("flexClass");
                resultLeft.appendChild(divResult4);
            } else if (i + 1 === 5) {
                const divP1 = document.createElement('p');
                const divP2 = document.createElement('p');
                divP1.textContent = `${i + 1}：`
                divP2.textContent = `${Q3.textContent}`;
                divResult5.appendChild(divP1);
                divResult5.appendChild(divP2);
                divResult5.classList.add("flexClass");
                resultLeft.appendChild(divResult5);
            } else if (i + 1 === 6) {
                const divP1 = document.createElement('p');
                const divP2 = document.createElement('p');
                divP1.textContent = `${i + 1}：`
                divP2.textContent = `${Q3.textContent}`;
                divResult6.appendChild(divP1);
                divResult6.appendChild(divP2);
                divResult6.classList.add("flexClass");
                resultLeft.appendChild(divResult6);
            } else if (i + 1 === 7) {
                const divP1 = document.createElement('p');
                const divP2 = document.createElement('p');
                divP1.textContent = `${i + 1}：`
                divP2.textContent = `${Q3.textContent}`;
                divResult7.appendChild(divP1);
                divResult7.appendChild(divP2);
                divResult7.classList.add("flexClass");
                resultLeft.appendChild(divResult7);
            } else if (i + 1 === 8) {
                const divP1 = document.createElement('p');
                const divP2 = document.createElement('p');
                divP1.textContent = `${i + 1}：`
                divP2.textContent = `${Q3.textContent}`;
                divResult8.appendChild(divP1);
                divResult8.appendChild(divP2);
                divResult8.classList.add("flexClass");
                resultLeft.appendChild(divResult8);
            } else if (i + 1 === 9) {
                const divP1 = document.createElement('p');
                const divP2 = document.createElement('p');
                divP1.textContent = `${i + 1}：`
                divP2.textContent = `${Q3.textContent}`;
                divResult9.appendChild(divP1);
                divResult9.appendChild(divP2);
                divResult9.classList.add("flexClass");
                resultLeft.appendChild(divResult9);
            } else if (i + 1 === 10) {
                const divP1 = document.createElement('p');
                const divP2 = document.createElement('p');
                divP1.textContent = `${i + 1}：`
                divP2.textContent = `${Q3.textContent}`;
                divResult10.appendChild(divP1);
                divResult10.appendChild(divP2);
                divResult10.classList.add("flexClass");
                resultLeft.appendChild(divResult10);
            }



            txtIndex = 0;
            newSpan.textContent = '';
            if (ModeSectFlag === 1) {
                i += 1;
                let n = textnums[i];
                Q1.textContent = `${textList[n]}`;
                Q2.textContent = `${textList2[n]}`;
                Q3.textContent = `${textList3[n]}`;
            } else {
                i += 1;
                let n = wordnums[i];
                Q1.textContent = `${wordList[n]}`;
                Q3.textContent = `${wordList3[n]}`;
            }
            if (Q3.textContent === 'undefined') {

                play.classList.add("NoneClass");
                result.classList.remove("NoneClass");
                resultLeft.classList.remove("NoneClass");
                resultRight.classList.remove("NoneClass");

                missList = Array.from(new Set(missList));
                for (let i = 0; i < missList.length; i++) {
                    miss += missList[i];
                    if (i < missList.length - 1) {
                        miss += ', ';
                    }
                }
                resultWeakKey.appendChild(p1);
                p1.textContent = `${miss}`;


                resultNumOfType.appendChild(p2);
                p2.textContent = `${typeCount}`;

                resultAccyracyRate.appendChild(p3);
                p3.textContent = `${Math.floor((typeCount - missCount) / typeCount * 100)}%`;

                resultTime.appendChild(p5);
                p5.textContent = `${timeCount}秒`;

                resultWPM.appendChild(p6);
                p6.textContent = `${Math.floor(typeCount / timeCount * 60)}`;

                resultScore.appendChild(p7);
                let score = Math.floor(((typeCount / timeCount * 60) * (((typeCount - missCount) / typeCount * 100) / 100) ** 3)); p7.textContent = `${score}`;

                resultLebel.appendChild(p8);
                if (score < 21) {
                    p8.textContent = 'E-';
                } else if (score < 38) {
                    p8.textContent = 'E';
                } else if (score < 55) {
                    p8.textContent = 'E+';
                } else if (score < 72) {
                    p8.textContent = 'D-';
                } else if (score < 89) {
                    p8.textContent = 'D';
                } else if (score < 106) {
                    p8.textContent = 'D+';
                } else if (score < 123) {
                    p8.textContent = 'C-';
                } else if (score < 140) {
                    p8.textContent = 'C';
                } else if (score < 157) {
                    p8.textContent = 'C+';
                } else if (score < 174) {
                    p8.textContent = 'B-';
                } else if (score < 191) {
                    p8.textContent = 'B';
                } else if (score < 208) {
                    p8.textContent = 'B+';
                } else if (score < 225) {
                    p8.textContent = 'A-';
                } else if (score < 242) {
                    p8.textContent = 'A';
                } else if (score < 259) {
                    p8.textContent = 'A+';
                } else if (score < 276) {
                    p8.textContent = 'S';
                } else {
                    p8.textContent = 'Good!';
                }


                if (timeFlag === true) {
                    timeCount = 0;
                    clearInterval(intarvald);
                    timeFlag = false;
                }

                i = 1;
                endressFlag = false;
                ModeSectFlag = -1;
                p4.textContent = `${missCount}`;
                resultMissNumOfType.appendChild(p4);

                if (username === '') {
                    username = 'ゲスト';
                }
                // タイムスタンプを追加して一意のキーを生成
                const timestamp = new Date().getTime();
                const uniqueKey = `${username}_${timestamp}`;
                localStorage.setItem(uniqueKey, score);
            }
        }
    }
});

// かぶりなしのランダムな数字
function getRandomNumbers(min, max, count) {
    let numbers = [];
    while (numbers.length < count) {
        let num = Math.floor(Math.random() * (max - min + 1)) + min;
        if (numbers.indexOf(num) === -1) {
            numbers.push(num);
        }
    }
    return numbers;
}

document.addEventListener("DOMContentLoaded", (event) => {
    let bgm = document.getElementById("bgm");
    bgm.volume = 0.5;  // 音量を設定
});


