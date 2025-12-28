## Conflict Resolution

When updating mappings, Stitch might encounter conflicts. This happens when a method inherits
multiple names from the previous version. Stitch will list all the options for you to choose from.

If you are re-generating the mappings, find the entry for the conflict in this file, and enter
the option that is written in **bold**. If the indices do not match what Stitch listed for you,
pick the option where the method inheritance matches the entry listed here. If there is no matching
method inheritance, report the issue [here](https://github.com/OrnitheMC/calamus/issues).

If you are generating new mappings, first check if the conflict can be resolved by an update to
our matches. If not, add a new entry for the conflict resolution to this file.

### b1.6-pre-trailer -> b1.5_02

ly.a(Lnx;IIII)Z: m_4533720 -> **m_8922194** (manual fix, name taken from b1.6-tb3)

### 12w32a/1.3.2 -> 12w34a

1) m_1605300 <- gv<-vg<-[java/lang/Object,vq<-java/lang/Object].a(I)Ljr;

**2) m_9124674 <- auk<-vg<-[java/lang/Object,vq<-java/lang/Object].a(I)Ljr;**

### 12w39b -> 12w40a

1) m_0560604 <- qd<-[kw<-java/lang/Object,qi<-java/lang/Object].c(DDDFF)V

**2) m_7650587 <- ql<-[kw<-java/lang/Object,qi<-java/lang/Object].c(DDDFF)V**

### 1.5.1 -> 13w16a-04192037

1) m_3275531 <- rc<-java/lang/Object(itf).aL()F

**2) m_9697920 <- nk<-ms<-java/lang/Object.aL()F**

### 14w10c/1.7.6 -> 14w11a

**1) apply <- bgy<-[java/lang/Object,com/google/common/base/Predicate<-java/lang/Object].a(Lbez;)Z, pg<-[java/lang/Object,com/google/common/base/Predicate<-java/lang/Object].a(Ljava/lang/String;)Z**

2) m_0863740 <- tr<-java/lang/Object(itf).a(Ltj;)Z

### 14w20b -> 14w21a

**1) m_5302345 <- nk<-java/lang/Object(itf).c()V, nn<-java/lang/Object(itf).c()V**

2) m_6095279 <- gd<-java/lang/Object(itf).c()V

### 14w28a -> 14w28b

1) m_0917416 <- bae<-java/lang/Object.c()V

**2) m_5302345 <- pb<-java/lang/Object(itf).c()V, pd<-java/lang/Object(itf).c()V**

### 16w39c -> 16w40a

1) m_5704843 <- bsq<-bsr<-bsg<-java/lang/Object.a(Lasu;DDDFI)V

**2) m_8730533 <- bsr<-bsg<-java/lang/Object.a(Lasu;DDDFI)V**

### 1.12-pre5 -> 1.12-pre6

1) m_2102188 <- bnl$a<-biy<-bip<-java/lang/Object.a(Lbhz;IIF)V

**2) m_3811351 <- bix<-bio<-java/lang/Object.a(Lbhz;IIF)V, biy<-bip<-java/lang/Object.a(Lbhz;IIF)V**

### 1.12.2 -> 17w43a

**1) m_6852870 <- net/minecraft/realms/RealmsEditBox<-net/minecraft/realms/RealmsGuiEventListener<-java/lang/Object.keyPressed(III)Z**

2) m_9152170 <- net/minecraft/realms/RealmsScreen<-java/lang/Object.keyPressed(III)Z

### 18w01a -> 18w02a

1) apply <- aaj$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaf;)Z, aaj$2<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaf;)Z, aaj$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaf;)Z, abr$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaf;)Z, abz$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaq;)Z, adt$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laap;)Z, adu$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaf;)Z, afb$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaq;)Z, afj$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaq;)Z, afl$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaf;)Z, agw$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaf;)Z, agz$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaf;)Z, aht$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lrq;)Z, ahu$b$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lajd;)Z, ahw$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaf;)Z, ahw$2<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaf;)Z, aia$b<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laap;)Z, aiq$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaf;)Z, ajd$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laie;)Z, amh$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laad;)Z, apl$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lanw;)Z, apo<-java/lang/Object.a(Lanw;)Z, apy<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lanw;)Z, auu$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbch;)Z, avd$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laaf;)Z, avk$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laug$a;)Z, axy$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laug$a;)Z, bci<-java/lang/Object.a(Lbch;)Z, bco<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbch;)Z, bcp<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbch;)Z, bcq<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbch;)Z, bfz$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbch;)Z, bot$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbnk;)Z, brc$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Ljava/lang/String;)Z, brh$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Ljava/lang/String;)Z, eg$a<-[java/lang/Enum<-[java/lang/Object,java/lang/constant/Constable<-java/lang/Object,java/lang/Comparable<-java/lang/Object,java/io/Serializable<-java/lang/Object],java/util/function/Predicate<-java/lang/Object,vr<-java/lang/Object].a(Leg;)Z, eg$c<-[java/lang/Enum<-[java/lang/Object,java/lang/constant/Constable<-java/lang/Object,java/lang/Comparable<-java/lang/Object,java/io/Serializable<-java/lang/Object],java/lang/Iterable<-java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Leg;)Z, ro$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laap;)Z, ru$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lrq;)Z, ru$2<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lrq;)Z

**2) test <- cg<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ch$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ch$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ci<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbck;)Z, cj$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbck;)Z, cj$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbck;)Z, cx<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), cz$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), cz$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), cz<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lanw;)Z, db$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lanw;)Z, db$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lanw;)Z**

### 18w05a -> 18w06a

1) m_2925147 <- bdo<-java/lang/Object.b(Lec;)Lbfj;, bgv<-[java/lang/Object,bgm<-[java/lang/Object,atb<-java/lang/Object]].b(Lec;)Lbfj;

**2) m_7852500 <- asn<-java/lang/Object(itf).b(Lec;)Lbfj;**

---

1) m_2404407 <- aty<-[java/lang/Object,ats<-[java/lang/Object,atq<-[java/lang/Object,atb<-java/lang/Object]]].a(Latv;Lec;)I

**2) m_5475075 <- atm<-[java/lang/Object,atn<-[java/lang/Object,atq<-[java/lang/Object,atb<-java/lang/Object],atu<-java/lang/Object],ats<-[java/lang/Object,atq<-[java/lang/Object,atb<-java/lang/Object]],java/lang/AutoCloseable<-java/lang/Object].a(Latv;Lec;)I**

---

1) m_4391494 <- bly<-bjo<-java/lang/Object.a(Latn;Lbgn;Ljava/util/Random;Lec;Lbjp;)Z

**2) m_5015587 <- bfl<-java/lang/Object.a(Latn;Lbgn;Ljava/util/Random;Lec;Lbjp;)Z, bjo<-java/lang/Object.a(Latn;Lbgn;Ljava/util/Random;Lec;Lbjp;)Z**

---

**1) m_1585233 <- bkv<-bly<-bjo<-java/lang/Object.e()Ljava/util/List;**

2) m_4444558 <- bkz<-bly<-bjo<-java/lang/Object.e()Ljava/util/List;

---

1) m_3210356 <- aug<-[java/lang/Object,op<-java/lang/Object].aa_()V

**2) m_5302345 <- ok<-java/lang/Object(itf).aa_()V, op<-java/lang/Object(itf).aa_()V**

### 18w07a -> 18w07b

1) apply <- agg$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z

**2) test <- abg$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z, abg$2<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z, abg$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z, abk$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), abk$2<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), abk$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), aco$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z, acs$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), acw$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labn;)Z, ada$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), aeq$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labm;)Z, aer$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z, aes$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labm;)Z, aev$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), aew$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), aex$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), afy$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labn;)Z, agd$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), agh$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labn;)Z, agj$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z, agm$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ago$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ahu$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z, ahx$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z, ahz$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), aic$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), air$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lrz;)Z, ais$b$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lakc;)Z, aiu$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z, aiu$2<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z, aiw$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), aix$b$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), aiy$b<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labm;)Z, aiz$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), aiz$2<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ajd$b<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ajp$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z, aju$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), akc$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lajc;)Z, akh$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ank$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labb;)Z, anp$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), aqp$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laoz;)Z, aqu$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), arb<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laoz;)Z, arg<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laoz;)Z, arg<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ayb$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbfs;)Z, ayh$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ayj$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labd;)Z, ayp$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ayq$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laxm$a;)Z, ayw$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), bbg$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laxm$a;)Z, bbm$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), bgb<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbfs;)Z, bgc<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbfs;)Z, bgd<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbfs;)Z, bgh<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbfs;)Z, bgh<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), bgi<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), bgj<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), blk$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbfs;)Z, bls$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), bxw$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbwn;)Z, bym$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), caj$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Ljava/lang/String;)Z, caz$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), cl<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbfv;)Z, cl<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), cm$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbfv;)Z, cm$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), cm$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbfv;)Z, cm$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), dc<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laoz;)Z, dc<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), de$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laoz;)Z, de$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), de$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Laoz;)Z, de$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ei$a<-[java/lang/Enum<-[java/lang/Object,java/lang/constant/Constable<-java/lang/Object,java/lang/Comparable<-java/lang/Object,java/io/Serializable<-java/lang/Object],java/util/function/Predicate<-java/lang/Object,wl<-java/lang/Object].a(Lei;)Z, ei$a<-[java/lang/Enum<-[java/lang/Object,java/lang/constant/Constable<-java/lang/Object,java/lang/Comparable<-java/lang/Object,java/io/Serializable<-java/lang/Object],java/util/function/Predicate<-java/lang/Object,wo<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ei$c<-[java/lang/Enum<-[java/lang/Object,java/lang/constant/Constable<-java/lang/Object,java/lang/Comparable<-java/lang/Object,java/io/Serializable<-java/lang/Object],java/lang/Iterable<-java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lei;)Z, ei$c<-[java/lang/Enum<-[java/lang/Object,java/lang/constant/Constable<-java/lang/Object,java/lang/Comparable<-java/lang/Object,java/io/Serializable<-java/lang/Object],java/lang/Iterable<-java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), rx$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Labm;)Z, sa$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), se$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lrz;)Z, se$2<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lrz;)Z, sh$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), sh$2<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge)**

### 18w10d -> 18w11a

1) m_4354222 <- aki<-ajs<-[acd<-abw<-abv<-abm<-[java/lang/Object,aan<-java/lang/Object,bn<-java/lang/Object],ajk<-[java/lang/Object,abl<-java/lang/Object]].r(Z)V

**2) m_6105103 <- aju<-java/lang/Object(itf).r(Z)V, ajv<-java/lang/Object(itf).r(Z)V**

### 18w16a -> 18w19a

**1) get <- ccs$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].get(I)Ljava/lang/Object;(bridge), chi$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].a(I)Lchi$a;**

2) m_9349353 <- ha<-gt<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],hj<-java/lang/Object].d(I)Lhj;

---

1) m_0215128 <- ha<-gt<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],hj<-java/lang/Object].b(ILhj;)Lhj;

**2) set <- ccs$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].set(ILjava/lang/Object;)Ljava/lang/Object;(bridge), chi$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].a(ILchi$a;)Lchi$a;**

---

1) m_3729040 <- ha<-gt<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],hj<-java/lang/Object].a(I)Lhj;

**2) remove <- ccs$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].remove(I)Ljava/lang/Object;(bridge), chi$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].b(I)Lchi$a;**

### 1.13 -> 18w30a

1) m_1097816 <- chz<-java/lang/Object(itf).getAdvance()F

**2) m_2263145 <- chx<-java/lang/Object(itf).getAdvance()F**

---

1) m_0993084 <- chz<-java/lang/Object(itf).getBoldOffset()F

**2) m_2954847 <- chx<-java/lang/Object(itf).getBoldOffset()F**

---

**1) m_6805892 <- chx<-java/lang/Object(itf).getShadowOffset()F**

2) m_8971395 <- chz<-java/lang/Object(itf).getShadowOffset()F

### 1.13.2 -> 18w43a

1) m_4833933 <- cdk<-java/lang/Object(itf).a(Lcdw;)Z

**2) test <- aeu$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), afk$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lafh;)Z, agd$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), agt$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lafh;)Z, ajz$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), akr$1<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lafr;)Z, amu$b<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), anc$b<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), anm$b<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lapb;)Z, anu$b<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lafq;)Z, aog$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), apb$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lanz;)Z, avh<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), awf<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lauc;)Z, bln<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lblz;)Z, bln<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), blo<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), blp<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), bmj<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lblz;)Z, bmk<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lblz;)Z, bml<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lblz;)Z, ct<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), cu$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), cu$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), cy<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbmd;)Z, cz$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbmd;)Z, cz$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lbmd;)Z, dl<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), dn$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), dn$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), dr<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lauc;)Z, dt$a<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lauc;)Z, dt$c<-[java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lauc;)Z, eq$a<-[java/lang/Enum<-[java/lang/Object,java/lang/constant/Constable<-java/lang/Object,java/lang/Comparable<-java/lang/Object,java/io/Serializable<-java/lang/Object],java/util/function/Predicate<-java/lang/Object,xv<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), eq$c<-[java/lang/Enum<-[java/lang/Object,java/lang/constant/Constable<-java/lang/Object,java/lang/Comparable<-java/lang/Object,java/io/Serializable<-java/lang/Object],java/lang/Iterable<-java/lang/Object,java/util/function/Predicate<-java/lang/Object].test(Ljava/lang/Object;)Z(bridge), ev$a<-[java/lang/Enum<-[java/lang/Object,java/lang/constant/Constable<-java/lang/Object,java/lang/Comparable<-java/lang/Object,java/io/Serializable<-java/lang/Object],java/util/function/Predicate<-java/lang/Object,yj<-java/lang/Object].a(Lev;)Z, ev$c<-[java/lang/Enum<-[java/lang/Object,java/lang/constant/Constable<-java/lang/Object,java/lang/Comparable<-java/lang/Object,java/io/Serializable<-java/lang/Object],java/lang/Iterable<-java/lang/Object,java/util/function/Predicate<-java/lang/Object].a(Lev;)Z**

---

1) m_4982900 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Lbpp$a;)Lbpp;

**2) m_6512460 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Lbpp$a;)Lbpp;**

---

**1) m_5056027 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Lbpp$a;[J)V**

2) m_5095466 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Lbpp$a;[J)V, bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Lbpp$a;[J)V

---

1) m_6555075 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Ljava/util/Map;)V, bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Ljava/util/Map;)V

**2) m_8332889 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Ljava/util/Map;)V**

--

**1) m_4863395 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Z)V**

2) m_5881503 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Z)V, bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Z)V

---

**1) m_2398547 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].b(J)V**

2) m_7218133 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].b(J)V

---

1) m_5280992 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].c()Ljava/util/Set;

**2) m_9627859 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].c()Ljava/util/Set;**

---

1) m_1337117 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].f()Ljava/util/Set;

**2) m_9580339 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].f()Ljava/util/Set;**

---

1) m_3423050 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].l()[Lit/unimi/dsi/fastutil/shorts/ShortList;

**2) m_9835953 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].l()[Lit/unimi/dsi/fastutil/shorts/ShortList;**

---

1) m_6079738 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].p()Lbor;

**2) m_9416441 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].p()Lbor;**

---

**1) m_0691793 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].q()J**

2) m_1913466 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].q()J

---

**1) m_0480678 <- bpr<-bnw<-[java/lang/Object,bnv<-java/lang/Object].a(IILbnu;)V**

2) m_9236571 <- bpt<-bnw<-[java/lang/Object,bnv<-java/lang/Object].a(IILbnu;)V

---

**1) m_7913440 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].b(Ljava/util/Map;)V**

2) m_8296251 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].b(Ljava/util/Map;)V, bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].b(Ljava/util/Map;)V

---

1) m_1732132 <- ez<-[java/lang/Object,ey<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]].a(I)Ljava/lang/Object;

**2) m_5378046 <- fc<-[java/lang/Object,et<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]](itf).a(I)Ljava/lang/Object;**

3) m_6589052 <- xu<-[java/lang/Object,ey<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]].a(I)Ljava/lang/Object;

### 18w49a -> 18w50a

1) m_6407734 <- bok<-[boj<-[bnq<-java/lang/Object,afu<-[java/lang/Object,afi<-[java/lang/Object,afg<-java/lang/Object,afv<-java/lang/Object],afp<-[java/lang/Object,afv<-java/lang/Object]]],afw<-java/lang/Object].f()Ljd;

**2) m_7534701 <- agv<-[java/lang/Object,afv<-java/lang/Object,bz<-java/lang/Object].f()Ljd;**

---

1) m_2177519 <- aps<-[aqf<-apb<-asg<-apv<-apu<-[ahl<-ahf<-ahe<-agv<-[java/lang/Object,afv<-java/lang/Object,bz<-java/lang/Object],apl<-[java/lang/Object,agu<-java/lang/Object]],apz<-java/lang/Object].dz()Z

**2) m_3448716 <- aqm<-apu<-[ahl<-ahf<-ahe<-agv<-[java/lang/Object,afv<-java/lang/Object,bz<-java/lang/Object],apl<-[java/lang/Object,agu<-java/lang/Object]].dz()Z**

3) m_9842230 <- apc<-[apu<-[ahl<-ahf<-ahe<-agv<-[java/lang/Object,afv<-java/lang/Object,bz<-java/lang/Object],apl<-[java/lang/Object,agu<-java/lang/Object]],apz<-java/lang/Object].dz()Z

---

1) m_3237423 <- aqn<-[aqm<-apu<-[ahl<-ahf<-ahe<-agv<-[java/lang/Object,afv<-java/lang/Object,bz<-java/lang/Object],apl<-[java/lang/Object,agu<-java/lang/Object]],aqt<-java/lang/Object].dM()Laqs;

**2) m_8826860 <- aqr<-[ags<-ahl<-ahf<-ahe<-agv<-[java/lang/Object,afv<-java/lang/Object,bz<-java/lang/Object],aho<-java/lang/Object,aqq<-[java/lang/Object,agu<-java/lang/Object],aqt<-java/lang/Object,bat<-java/lang/Object].dM()Laqs;**

---

**1) m_7903307 <- bok<-[boj<-[bnq<-java/lang/Object,afu<-[java/lang/Object,afi<-[java/lang/Object,afg<-java/lang/Object,afv<-java/lang/Object],afp<-[java/lang/Object,afv<-java/lang/Object]]],afw<-java/lang/Object].a(Ljd;)V**

2) m_9488819 <- bnl<-bok<-[boj<-[bnq<-java/lang/Object,afu<-[java/lang/Object,afi<-[java/lang/Object,afg<-java/lang/Object,afv<-java/lang/Object],afp<-[java/lang/Object,afv<-java/lang/Object]]],afw<-java/lang/Object].a(Ljd;)V

---

**1) m_1005909 <- dam<-[cym<-czc<-java/lang/Object,dje<-java/lang/Object,dlf<-java/lang/Object].a()Lday;**

2) m_6895656 <- cyu<-[cym<-czc<-java/lang/Object,dhw<-java/lang/Object,dje<-java/lang/Object].a()Lday;

### 19w02a -> 19w03a

**1) get <- crj$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].get(I)Ljava/lang/Object;(bridge), cro$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].a(I)Lcro$a;, hr<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ij<-java/lang/Object].get(I)Ljava/lang/Object;(bridge), hr<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ij<-java/lang/Object].k(I)Lih;**

2) m_4405511 <- hn<-hp<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ih<-java/lang/Object].a(I)Lho;

3) m_5126743 <- hx<-hp<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ih<-java/lang/Object].a(I)Lhy;

4) m_8509821 <- hu<-hp<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ih<-java/lang/Object].a(I)Lhv;

---

1) m_3125067 <- hw<-hp<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ih<-java/lang/Object].d(ILih;)Lih;

**2) set <- crj$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].set(ILjava/lang/Object;)Ljava/lang/Object;(bridge), cro$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].a(ILcro$a;)Lcro$a;, hr<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ij<-java/lang/Object].set(ILjava/lang/Object;)Ljava/lang/Object;(bridge)**

---

1) m_8339536 <- hp<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ih<-java/lang/Object].c(I)Lih;, hr<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ij<-java/lang/Object].c(I)Lih;

**2) remove <- crj$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].remove(I)Ljava/lang/Object;(bridge), cro$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].b(I)Lcro$a;, hy<-hr<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ij<-java/lang/Object].remove(I)Ljava/lang/Object;(bridge)**

---

**1) add <- crj$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].add(ILjava/lang/Object;)V(bridge), cro$b<-java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]].b(ILcro$a;)V**

2) m_3125067 <- hy<-hr<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ij<-java/lang/Object].add(ILjava/lang/Object;)V(bridge)

3) set <- hp<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ih<-java/lang/Object].c(ILih;)V, hp<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ih<-java/lang/Object].c(ILih;)V(bridge), hr<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ij<-java/lang/Object].c(ILih;)V, hr<-[java/util/AbstractList<-[java/util/AbstractCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]],java/util/List<-[java/lang/Object,java/util/SequencedCollection<-[java/lang/Object,java/util/Collection<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]]]],ij<-java/lang/Object].c(ILih;)V(bridge)

### 19w07a -> 19w08a

1) m_0049367 <- csd<-[crq<-java/lang/Object,css<-java/lang/Object,csv<-java/lang/Object].a(IIF)V

2) m_0498464 <- csa<-csg<-[crd<-java/lang/Object,csi<-[java/lang/Object,csh<-java/lang/Object]].a(IIF)V, csn<-[cst<-[crq<-java/lang/Object,csu<-[java/lang/Object,csw<-[java/lang/Object,csv<-java/lang/Object]]],css<-java/lang/Object].a(IIF)V

3) m_2686018 <- csf<-[crq<-java/lang/Object,css<-java/lang/Object,csv<-java/lang/Object].a(IIF)V

**4) m_3956703 <- cut<-[csg<-[crd<-java/lang/Object,csi<-[java/lang/Object,csh<-java/lang/Object]],ctw<-java/lang/Object].a(IIF)V, cvi<-[cst<-[crq<-java/lang/Object,csu<-[java/lang/Object,csw<-[java/lang/Object,csv<-java/lang/Object]]],css<-java/lang/Object,cuk<-java/lang/Object].a(IIF)V**

5) m_5337651 <- cxy<-[crq<-java/lang/Object,css<-java/lang/Object,csv<-java/lang/Object].a(IIF)V

6) m_6827666 <- crz<-[crq<-java/lang/Object,css<-java/lang/Object,csv<-java/lang/Object].a(IIF)V

7) m_9525120 <- cxz<-[crq<-java/lang/Object,css<-java/lang/Object,csv<-java/lang/Object,cye<-java/lang/Object,qe<-java/lang/Object].a(IIF)V

---

1) m_2291416 <- wn<-[java/lang/Object,wt<-java/lang/Object].a(Lvw;)V

**2) m_9570331 <- wx<-[java/lang/Object,wr<-[java/lang/Object,wt<-java/lang/Object]].a(Lvw;)V**

### 19w08b -> 19w09a

**1) m_5349631 <- asv<-[ahm<-[java/lang/Object,agl<-java/lang/Object,bz<-java/lang/Object],aso<-java/lang/Object].a(Lahm;FFFFF)V**

2) m_5487055 <- asd<-[ahm<-[java/lang/Object,agl<-java/lang/Object,bz<-java/lang/Object],aso<-java/lang/Object].a(Lahm;FFFFF)V

### 1.14.4-pre3 -> 1.14.4-pre4

1) m_4859862 <- wc<-[java/lang/Object,nu<-[java/lang/Object,jh<-java/lang/Object]].a()Ljc;

**2) m_5397109 <- dkc<-[java/lang/Object,kf<-[java/lang/Object,jh<-java/lang/Object]].a()Ljc;**

