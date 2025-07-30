"use strict";

// プロフィール
// 要素取得
const IntroductionBtn = document.getElementById('IntroductionBtn');
const SkillBtn = document.getElementById('SkillBtn');
const RamanBtn = document.getElementById('RamanBtn');
const DevelopBtn = document.getElementById('DevelopBtn');
// ハンバーガーメニュー
const hamburgerMenuImg = document.getElementById('hamburgerMenuImg');
const hamburgerMenuP1 = document.getElementById('hamburgerMenuP1');
const hamburgerMenuP2 = document.getElementById('hamburgerMenuP2');
const hamburgerMenuP3 = document.getElementById('hamburgerMenuP3');
const hamburgerMenuP4 = document.getElementById('hamburgerMenuP4');
const hamburgerMenuP5 = document.getElementById('hamburgerMenuP5');

// ページ遷移実装
IntroductionBtn.addEventListener('click', function () {
    const target = document.getElementById('introductionSection');
    if (target) target.scrollIntoView({ behavior: 'smooth' });
});
SkillBtn.addEventListener('click', function () {
    const target = document.getElementById('skillSection');
    if (target) target.scrollIntoView({ behavior: 'smooth' });
});
RamanBtn.addEventListener('click', function () {
    const target = document.getElementById('ramanhistorySection');
    if (target) target.scrollIntoView({ behavior: 'smooth' });
});
DevelopBtn.addEventListener('click', function () {
    const target = document.getElementById('developmentSection');
    if (target) target.scrollIntoView({ behavior: 'smooth' });
});
// ホバー実装
IntroductionBtn.addEventListener('mouseover', function () {
    IntroductionBtn.style.cursor = 'pointer';
    IntroductionBtn.textContent = '▶自己紹介';
});
IntroductionBtn.addEventListener('mouseout', function () {
    IntroductionBtn.textContent = '　自己紹介';

});
SkillBtn.addEventListener('mouseover', function () {
    SkillBtn.style.cursor = 'pointer';
    SkillBtn.textContent = '▶スキル'
});
SkillBtn.addEventListener('mouseout', function () {
    SkillBtn.textContent = '　スキル'
});
RamanBtn.addEventListener('mouseover', function () {
    RamanBtn.style.cursor = 'pointer';
    RamanBtn.textContent = '▶ラーメン'
});
RamanBtn.addEventListener('mouseout', function () {
    RamanBtn.textContent = '　ラーメン'
});
DevelopBtn.addEventListener('mouseover', function () {
    DevelopBtn.style.cursor = 'pointer';
    DevelopBtn.textContent = '▶開発物'
});
DevelopBtn.addEventListener('mouseout', function () {
    DevelopBtn.textContent = '　開発物'
});

$('.Top_slider').slick({
    slidesToShow: 9,
    slidesToScroll: 1,
    asNavFor: '.Second_slider',
    dots: true,
    centerMode: true,
    focusOnSelect: true,
});

$('.Second_slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    prevArrow: '<button class="slick-prev"><img src="./img/left.png" alt="Prev"></button>',
    nextArrow: '<button class="slick-next"><img src="./img/right.png" alt="Next"></button>',
    fade: true,
    asNavFor: '.Top_slider'
});


const texts1 = ["『桜木屋』", "『孝百』", "『寿』", "『菅野食堂』", "『ひぐま屋』", "『麵屋　いおり』", "『はてな』"]; // 変更したいテキストの配列
const texts2 = ["秋田県", "秋田県", "秋田県", "秋田県", "盛岡市", "盛岡市", "盛岡市"]; // 変更したいテキストの配列
// const texts3 = ["思い出深い時期：小・中・高・現在", "思い出深い時期：高・現在", "思い出深い時期：小・中・高・現在", "思い出深い時期：現在", "思い出深い時期：現在", "思い出深い時期：現在", "思い出深い時期：小・中・高・現在"]; // 変更したいテキストの配列
const texts4 = ["スキー場の近くにあります。クロスカントリースキー部だった小学生時代に、部活帰りに食べた一杯が冷え切った体を温めてくれました。人生ではじめ何かを頑張ろうと思いスキー部を始めた時期でした。最後の大会ではたくさん練習したにもかかわらず転んでしまい、いい結果ではありませんでした。しかし一生懸命取り組んだことは一生の宝です。その挑戦経て、今でも私は大変なことにも立ち向かえます。"
    , "とても小さいころから家族でよく食べていましたが、高校時代がピークで食べてました。テニス場の近くにあり、部活帰りはみんなで食べに行っていました。硬式テニス部だったはずが、ラーメン部になっていたのはいい思い出です。ほかにも思い出深いエピソードは多く、この店は私の高校時代を象徴します。"
    , "高校時代の夏休みに母親と訪れたのがいい思い出です。近くには車の洗車場があり、水の出るホースで洗車を手伝いました。車の中のクーラーが気持ちよかったことなど、涼しい思い出と繋がって記憶している店です。母校は進学校でした。夏休みの課題は難易度が適切で、一筋縄で解けませんでした。暑さと難問を解けない焦りの中で避暑地的な存在はとても励みになっていました。"
    , "高校時代のテスト期間中に友人と食べていました。近くには図書館があり、そこで友人と勉強をしたのちにラーメンを食べるというルーティンがお決まりでした。一人ではなかなか勉強がはかどらない時でも、協力して取り組めば効率はいいというものです。ご褒美のラーメンがあったことも、勉強を頑張る一助になっていたかもしれません。"
    , "専門学生としての生活も慣れてきた1年目くらいでたどり着いた至高のラーメン屋です。就職活動や学校の課題に取り組んでいた時期でした。そんな中で、ラーメン屋の暖かい雰囲気と美味しいラーメンが心を癒してくれました。"
    , "地元でよく食べていた煮干しラーメンが恋しくなり、盛岡市に引っ越してきた際に訪れました。スープやトッピングが違い、地元のらーめとはまた違いましたが、環境の変化をやんわりと伝えられたようで新天地で頑張る覚悟をもらいました。"
    , "盛岡に来て初めて食べたラーメンです。新しい環境に慣れていない中でできた数人の友達と訪れました。初めてお店で食べる油そばはとめも新鮮でした。"]; // 変更したいテキストの配列
// const texts5 = ["感想：", "感想：", "感想：", "感想：", "感想：", "感想："]; // 変更したいテキストの配列
const texts6 = ["ニラそばや肉そばは言わずもがな美味しいですが。テーブルにあるフリーのニンニクを足すことでさらにパンチがまして満足度が向上します。それに対して、ノーマルの醤油ラーメンや塩ラーメンもさっぱりと食べれて最高です。また、唐揚げがとても大きく衣がサクサクです。唐揚げは食べきれない場合には持ち帰ることもできます。"
    , "店内に充満した煮干しの香り、中毒性の高い濃い煮干しのだし、もちもちでスープを絡めとる麺、食券性で会計がしやすいシステム、チャーシュー丼付きのラーメンを手ごろな価格で食べれる学生セット。この店は、私のラーメン人生を変えたと言っても過言ではありません。"
    , "ニンニクラーメンと言うメニューがあります。名前の通りパンチ力は絶大です。チャーシューも柔らかくもやしとニラがたっぷり入っていて、ボリュームも満点です。さらに、スープの味も濃いめで、ニンニクの風味が食欲をそそります。また、ラーメンではありませんが生姜焼き定食もおすすめです。"
    , "私は醤油ラーメンとチャーハンを注文することを推します。醬油ラーメンはあっさりとしたスープですが、塩コショウがよく効いています。そしてチャーハンがラーメンとよく合うんです。ラーメンのスープとチャーハンを口内調味することで、より一層美味しさが増します。"
    , "魚介系のスープはよくありますが、エビラーメンは少ないと思います。エビの風味がいいのはさることながら、スープにエビのかけらが沈んでいます。エビ好きなら一度は味わってほしい逸品です。スープはエビだけでなく味噌で味付けされていて、濃厚な味わいが楽しめます。チャーシューもふわふわで美味しく、さらにひき肉のような肉も入っていて、それが麺に絡まって口に入ってくるので食べ応え抜群です。"
    , "盛岡市のラーメン屋の中でも、特におすすめの一杯です。煮干しのスープが特徴的です。濃厚でトロトロとしていて油そばのように感じます。面に絡みついてとてもおいしいです。"
    , "ペチカ麵という特殊な縮れた面があります。油がしっかり絡みつきます。大もりまでは通常料金と同じでお得ですが、たくさん食べれる人向けです。"
    ]; // 変更したいテキストの配列

$('.Top_slider').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
    $('#text-content1').text(texts1[nextSlide]); // 次のスライドに対応するテキストを表示
});
$('.Top_slider').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
    $('#text-content2').text(texts2[nextSlide]); // 次のスライドに対応するテキストを表示
});
// $('.Top_slider').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
//     $('#text-content3').text(texts3[nextSlide]); // 次のスライドに対応するテキストを表示
// });
$('.Top_slider').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
    $('#text-content4').text(texts4[nextSlide]); // 次のスライドに対応するテキストを表示
});
// $('.Top_slider').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
//     $('#text-content5').text(texts5[nextSlide]); // 次のスライドに対応するテキストを表示
// });
$('.Top_slider').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
    $('#text-content6').text(texts6[nextSlide]); // 次のスライドに対応するテキストを表示
});

// 評価詳細ボタン
document.addEventListener('DOMContentLoaded', function () {
    const detailBtn = document.getElementById('detailEvaluationBtn');
    const sourceTable = document.getElementById('sourceTable');
    if (detailBtn && sourceTable) {
        detailBtn.addEventListener('click', function () {
            sourceTable.classList.toggle('show');
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const detailBtn = document.getElementById('detailEvaluationBtn2');
    const sourceTable = document.getElementById('sourceTable2');
    if (detailBtn && sourceTable) {
        detailBtn.addEventListener('click', function () {
            sourceTable.classList.toggle('show');
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const detailBtn = document.getElementById('detailEvaluationBtn3');
    const sourceTable = document.getElementById('sourceTable3');
    if (detailBtn && sourceTable) {
        detailBtn.addEventListener('click', function () {
            sourceTable.classList.toggle('show');
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const detailBtn = document.getElementById('detailEvaluationBtn4');
    const sourceTable = document.getElementById('sourceTable4');
    if (detailBtn && sourceTable) {
        detailBtn.addEventListener('click', function () {
            sourceTable.classList.toggle('show');
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const detailBtn = document.getElementById('detailEvaluationBtn5');
    const sourceTable = document.getElementById('sourceTable5');
    if (detailBtn && sourceTable) {
        detailBtn.addEventListener('click', function () {
            sourceTable.classList.toggle('show');
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const detailBtn = document.getElementById('detailEvaluationBtn6');
    const sourceTable = document.getElementById('sourceTable6');
    if (detailBtn && sourceTable) {
        detailBtn.addEventListener('click', function () {
            sourceTable.classList.toggle('show');
        });
    }
});