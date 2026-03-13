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

ly.a(Lnx;IIII)Z: m_84533720 -> **m_28922194** (manual fix, name taken from b1.6-tb3)

### 12w32a/1.3.2 -> 12w34a

1) m_51605300 <- gv<-ux<-[java/lang/Object,vh<-java/lang/Object].a(I)Ljr;

**2) m_99124674 <- atw<-ux<-[java/lang/Object,vh<-java/lang/Object].a(I)Ljr;**

### 12w39b -> 12w40a

**1) m_57650587 <- pi<-ju<-java/lang/Object.c(DDDFF)V**

2) m_70560604 <- pb<-ju<-java/lang/Object.c(DDDFF)V

### 1.5.1 -> 13w16a-04192037

**1) m_09697920 <- ng<-mp<-java/lang/Object.aL()F**

2) m_43275531 <- qv<-java/lang/Object(itf).aL()F, rb<-[sb<-[nr<-ng<-mp<-java/lang/Object,rw<-[java/lang/Object,mn<-java/lang/Object]],qv<-java/lang/Object,sd<-java/lang/Object].aL()F

### 14w20b -> 14w21a

**1) m_65302345 <- nk<-java/lang/Object(itf).c()V**

2) m_66095279 <- gd<-java/lang/Object(itf).c()V

### 14w28a -> 14w28b

1) m_60917416 <- bae<-java/lang/Object.c()V

**2) m_65302345 <- pb<-java/lang/Object(itf).c()V**

### 16w39c -> 16w40a

1) m_15704843 <- bsr<-bsh<-java/lang/Object.a(Lasu;DDDFI)V

**2) m_88730533 <- bss<-bsh<-java/lang/Object.a(Lasu;DDDFI)V**

### 1.12-pre5 -> 1.12-pre6

1) m_32102188 <- bnn$a<-java/lang/Object.a(Lbhz;IIF)V

**2) m_43811351 <- bix<-bio<-java/lang/Object.a(Lbhz;IIF)V**

### 1.12.2 -> 17w43a

1) m_09152170 <- net/minecraft/realms/RealmsScreen<-java/lang/Object.keyPressed(III)Z

**2) m_56852870 <- net/minecraft/realms/RealmsEditBox<-java/lang/Object.keyPressed(III)Z**

### 18w05a -> 18w06a

**1) m_77852500 <- asn<-java/lang/Object(itf).b(Lec;)Lbfj;**

2) m_92925147 <- bdo<-java/lang/Object.b(Lec;)Lbfj;, bgv<-[java/lang/Object,bgm<-[java/lang/Object,atb<-java/lang/Object]].b(Lec;)Lbfj;

---

**1) m_15475075 <- asj<-[java/lang/Object,asn<-java/lang/Object].a(Latv;Lec;)I**

2) m_42404407 <- ass<-[java/lang/Object,asn<-java/lang/Object].a(Latv;Lec;)I

---

1) m_44391494 <- bhm<-bes<-java/lang/Object.a(Latn;Lbgn;Ljava/util/Random;Lec;Lbjp;)Z

**2) m_85015587 <- bfl<-java/lang/Object.a(Latn;Lbgn;Ljava/util/Random;Lec;Lbjp;)Z**

---

**1) m_81585233 <- bhe<-bhm<-bes<-java/lang/Object.e()Ljava/util/List;**

2) m_94444558 <- bhg<-bhm<-bes<-java/lang/Object.e()Ljava/util/List;

---

1) m_63210356 <- ata<-java/lang/Object.aa_()V

**2) m_65302345 <- ok<-java/lang/Object(itf).aa_()V**

### 18w10d -> 18w11a

1) m_44354222 <- akh<-ajr<-[acd<-abw<-abv<-abm<-[java/lang/Object,aan<-java/lang/Object,bn<-java/lang/Object],ajj<-[java/lang/Object,abl<-java/lang/Object]].r(Z)V

**2) m_86105103 <- aju<-java/lang/Object(itf).r(Z)V**

### 1.13 -> 18w30a

1) m_21097816 <- cia<-java/lang/Object(itf).getAdvance()F

**2) m_92263145 <- chx<-java/lang/Object(itf).getAdvance()F**

---

1) m_30993084 <- cia<-java/lang/Object(itf).getBoldOffset()F

**2) m_32954847 <- chx<-java/lang/Object(itf).getBoldOffset()F**

---

1) m_68971395 <- cia<-java/lang/Object(itf).getShadowOffset()F

**2) m_96805892 <- chx<-java/lang/Object(itf).getShadowOffset()F**

### 1.13.2 -> 18w43a

**1) m_26512460 <- bnj<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Lbpp$a;)Lbpp;**

2) m_44982900 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Lbpp$a;)Lbpp;

---

1) m_75095466 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Lbpp$a;[J)V

**2) m_85056027 <- bnj<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Lbpp$a;[J)V**

---

**1) m_08332889 <- bnj<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Ljava/util/Map;)V**

2) m_46555075 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Ljava/util/Map;)V

---

**1) m_04863395 <- bnj<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Z)V**

2) m_95881503 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Z)V

---

**1) m_12398547 <- bnj<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].b(J)V**

2) m_87218133 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].b(J)V

---

**1) m_09627859 <- bnj<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].c()Ljava/util/Set;**

2) m_85280992 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].c()Ljava/util/Set;

---

**1) m_39580339 <- bnj<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].f()Ljava/util/Set;**

2) m_81337117 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].f()Ljava/util/Set;

---

1) m_03423050 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].l()[Lit/unimi/dsi/fastutil/shorts/ShortList;

**2) m_19835953 <- bnj<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].l()[Lit/unimi/dsi/fastutil/shorts/ShortList;**

---

1) m_06079738 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].p()Lbor;

**2) m_79416441 <- bnj<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].p()Lbor;**

---

1) m_01913466 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].q()J

**2) m_90691793 <- bnj<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].q()J**

---

**1) m_10480678 <- bot<-bmz<-[java/lang/Object,bmy<-java/lang/Object].a(IILbnu;)V**

2) m_79236571 <- bov<-bmz<-[java/lang/Object,bmy<-java/lang/Object].a(IILbnu;)V

---

1) m_68296251 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].b(Ljava/util/Map;)V

**2) m_77913440 <- bnj<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].b(Ljava/util/Map;)V**

---

1) m_06589052 <- xg<-[java/lang/Object,et<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]].a(I)Ljava/lang/Object;

**2) m_15378046 <- fc<-[java/lang/Object,et<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]](itf).a(I)Ljava/lang/Object;**

3) m_91732132 <- eu<-[java/lang/Object,et<-[java/lang/Object,java/lang/Iterable<-java/lang/Object]].a(I)Ljava/lang/Object;

### 18w49a -> 18w50a

1) m_26407734 <- bnk<-[bnj<-[bmq<-java/lang/Object,afj<-[java/lang/Object,aex<-[java/lang/Object,aev<-java/lang/Object,afk<-java/lang/Object],afe<-[java/lang/Object,afk<-java/lang/Object]]],afl<-java/lang/Object].f()Ljd;

**2) m_57534701 <- agk<-[java/lang/Object,afk<-java/lang/Object,bz<-java/lang/Object].f()Ljd;**

---

1) m_82177519 <- aph<-[apu<-aoq<-arn<-apk<-apj<-[aha<-agu<-agt<-agk<-[java/lang/Object,afk<-java/lang/Object,bz<-java/lang/Object],apa<-[java/lang/Object,agj<-java/lang/Object]],apo<-java/lang/Object].dz()Z

2) m_89842230 <- aor<-[apj<-[aha<-agu<-agt<-agk<-[java/lang/Object,afk<-java/lang/Object,bz<-java/lang/Object],apa<-[java/lang/Object,agj<-java/lang/Object]],apo<-java/lang/Object].dz()Z

**3) m_93448716 <- aqb<-apj<-[aha<-agu<-agt<-agk<-[java/lang/Object,afk<-java/lang/Object,bz<-java/lang/Object],apa<-[java/lang/Object,agj<-java/lang/Object]].dz()Z**

---

1) m_13237423 <- aqc<-aqb<-apj<-[aha<-agu<-agt<-agk<-[java/lang/Object,afk<-java/lang/Object,bz<-java/lang/Object],apa<-[java/lang/Object,agj<-java/lang/Object]].dM()Laqs;

**2) m_18826860 <- aqg<-[agh<-aha<-agu<-agt<-agk<-[java/lang/Object,afk<-java/lang/Object,bz<-java/lang/Object],ahd<-java/lang/Object,aqf<-[java/lang/Object,agj<-java/lang/Object],azw<-java/lang/Object].dM()Laqs;**

---

**1) m_57903307 <- bnk<-[bnj<-[bmq<-java/lang/Object,afj<-[java/lang/Object,aex<-[java/lang/Object,aev<-java/lang/Object,afk<-java/lang/Object],afe<-[java/lang/Object,afk<-java/lang/Object]]],afl<-java/lang/Object].a(Ljd;)V**

2) m_99488819 <- bml<-bnj<-[bmq<-java/lang/Object,afj<-[java/lang/Object,aex<-[java/lang/Object,aev<-java/lang/Object,afk<-java/lang/Object],afe<-[java/lang/Object,afk<-java/lang/Object]]].a(Ljd;)V

---

1) m_16895656 <- cxg<-cxo<-java/lang/Object.a()Lday;

**2) m_31005909 <- cyy<-cxo<-java/lang/Object.a()Lday;**

### 19w07a -> 19w08a

1) m_15337651 <- cxj<-[crd<-java/lang/Object,csh<-java/lang/Object].a(IIF)V

2) m_16827666 <- crm<-[crd<-java/lang/Object,csh<-java/lang/Object].a(IIF)V

3) m_30049367 <- crq<-[crd<-java/lang/Object,csh<-java/lang/Object].a(IIF)V

4) m_32686018 <- crs<-[crd<-java/lang/Object,csh<-java/lang/Object].a(IIF)V

5) m_60498464 <- csa<-csg<-[crd<-java/lang/Object,csi<-[java/lang/Object,csh<-java/lang/Object]].a(IIF)V

6) m_89525120 <- cxk<-[crd<-java/lang/Object,csh<-java/lang/Object,cxp<-java/lang/Object,qd<-java/lang/Object].a(IIF)V

**7) m_93956703 <- cut<-[csg<-[crd<-java/lang/Object,csi<-[java/lang/Object,csh<-java/lang/Object]],ctw<-java/lang/Object].a(IIF)V**

---

1) m_82291416 <- wn<-[java/lang/Object,wt<-java/lang/Object].a(Lvw;)V

**2) m_89570331 <- ww<-[java/lang/Object,wr<-[java/lang/Object,wt<-java/lang/Object]].a(Lvw;)V**

### 19w08b -> 19w09a

**1) m_65349631 <- asv<-[ahm<-[java/lang/Object,agl<-java/lang/Object,bz<-java/lang/Object],aso<-java/lang/Object].a(Lahm;FFFFF)V**

2) m_75487055 <- asd<-[ahm<-[java/lang/Object,agl<-java/lang/Object,bz<-java/lang/Object],aso<-java/lang/Object].a(Lahm;FFFFF)V

### 1.14.4-pre3 -> 1.14.4-pre4

1) m_04859862 <- wb<-[java/lang/Object,nt<-[java/lang/Object,jh<-java/lang/Object]].a()Ljc;

**2) m_35397109 <- dka<-[java/lang/Object,kf<-[java/lang/Object,jh<-java/lang/Object]].a()Ljc;**

