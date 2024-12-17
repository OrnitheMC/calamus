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

ly.a(Lnx;IIII)Z: m_7925651 -> **m_8199947** (manual fix, name taken from b1.6-tb3)

### 12w39b -> 12w40a

**1) m_8108915 <- ql<-[kw<-java/lang/Object,qi<-java/lang/Object].c(DDDFF)V**

2) m_8813677 <- qd<-[kw<-java/lang/Object,qi<-java/lang/Object].c(DDDFF)V

### 1.5.1 -> 13w16a-04192037

**1) m_4971784 <- nk<-ms<-java/lang/Object.aL()F**

2) m_9161906 <- rc<-java/lang/Object(itf).aL()F

### 14w20b -> 14w21a

1) m_3056365 <- gd<-java/lang/Object(itf).c()V

**2) m_5506965 <- nk<-java/lang/Object(itf).c()V, nn<-java/lang/Object(itf).c()V**

### 14w28a -> 14w28b

1) m_1420044 <- bae<-java/lang/Object.c()V

**2) m_5506965 <- pb<-java/lang/Object(itf).c()V, pd<-java/lang/Object(itf).c()V**

### 1.10.2 -> 16w32a

1) m_0054836 <- aeo$7<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

2) m_0074173 <- aeo$6<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

3) m_1264601 <- aeo$3<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

**4) m_2708149 <- aez$1<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;**

5) m_4178545 <- aeo$9<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

6) m_4539558 <- aeo$11<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

7) m_5190968 <- aeo$14<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

8) m_6263986 <- aeo$10<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

9) m_6402606 <- aeo$21<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

10) m_6665253 <- aeo$19<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

11) m_7010000 <- aeo$5<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

12) m_7544376 <- aeo$17<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

13) m_7853793 <- aeo$20<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

14) m_8660281 <- aeo$2<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

15) m_8843097 <- aeo$13<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

16) m_8904905 <- aeo$18<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

17) m_9725227 <- aeo$8<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

18) m_9807816 <- aeo$4<-[java/lang/Object,aez$a<-java/lang/Object].a(Laeq;)Ljava/lang/String;

### 16w39c -> 16w40a

**1) m_4020455 <- bsr<-bsg<-java/lang/Object.a(Lasu;DDDFI)V**

2) m_8437148 <- bsq<-bsr<-bsg<-java/lang/Object.a(Lasu;DDDFI)V

### 1.12-pre5 -> 1.12-pre6

**1) m_3845983 <- bix<-bio<-java/lang/Object.a(Lbhz;IIF)V, biy<-bip<-java/lang/Object.a(Lbhz;IIF)V**

2) m_8193356 <- bnl$a<-biy<-bip<-java/lang/Object.a(Lbhz;IIF)V

### 1.12.2 -> 17w43a

**1) m_0860186 <- net/minecraft/realms/RealmsEditBox<-net/minecraft/realms/RealmsGuiEventListener<-java/lang/Object.keyPressed(III)Z**

2) m_7937999 <- net/minecraft/realms/RealmsScreen<-java/lang/Object.keyPressed(III)Z

### 18w05a -> 18w06a

**1) m_4919395 <- asn<-java/lang/Object(itf).b(Lec;)Lbfj;**

2) m_9971171 <- bdo<-java/lang/Object.b(Lec;)Lbfj;, bgv<-[java/lang/Object,bgm<-[java/lang/Object,atb<-java/lang/Object]].b(Lec;)Lbfj;

---

**1) m_1517868 <- atm<-[java/lang/Object,atn<-[java/lang/Object,atq<-[java/lang/Object,atb<-java/lang/Object],atu<-java/lang/Object],ats<-[java/lang/Object,atq<-[java/lang/Object,atb<-java/lang/Object]],java/lang/AutoCloseable<-java/lang/Object].a(Latv;Lec;)I**

2) m_6502512 <- aty<-[java/lang/Object,ats<-[java/lang/Object,atq<-[java/lang/Object,atb<-java/lang/Object]]].a(Latv;Lec;)I

---

**1) m_2665009 <- bfl<-java/lang/Object.a(Latn;Lbgn;Ljava/util/Random;Lec;Lbjp;)Z, bjo<-java/lang/Object.a(Latn;Lbgn;Ljava/util/Random;Lec;Lbjp;)Z**

2) m_4632275 <- bly<-bjo<-java/lang/Object.a(Latn;Lbgn;Ljava/util/Random;Lec;Lbjp;)Z

---

1) m_8161543 <- bkz<-bly<-bjo<-java/lang/Object.e()Ljava/util/List;

**2) m_9912401 <- bkv<-bly<-bjo<-java/lang/Object.e()Ljava/util/List;**

---

**1) m_5506965 <- ok<-java/lang/Object(itf).aa_()V, op<-java/lang/Object(itf).aa_()V**

2) m_8716168 <- aug<-[java/lang/Object,op<-java/lang/Object].aa_()V

### 18w10d -> 18w11a

**1) m_6542542 <- aju<-java/lang/Object(itf).r(Z)V, ajv<-java/lang/Object(itf).r(Z)V**

2) m_7941291 <- aki<-ajs<-[acd<-abw<-abv<-abm<-[java/lang/Object,aan<-java/lang/Object,bn<-java/lang/Object],ajk<-[java/lang/Object,abl<-java/lang/Object]].r(Z)V

### 1.13 -> 18w30a

**1) m_7423871 <- chx<-java/lang/Object(itf).getAdvance()F**

2) m_8530833 <- chz<-java/lang/Object(itf).getAdvance()F

---

1) m_0831354 <- chz<-java/lang/Object(itf).getBoldOffset()F

**2) m_1020198 <- chx<-java/lang/Object(itf).getBoldOffset()F**

---

**1) m_4192644 <- chx<-java/lang/Object(itf).getShadowOffset()F**

2) m_6194748 <- chz<-java/lang/Object(itf).getShadowOffset()F

### 1.13.2 -> 18w43a

1) m_3504345 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Lbpp$a;)Lbpp;

**2) m_6941329 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Lbpp$a;)Lbpp;**

---

**1) m_3098180 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Lbpp$a;[J)V**

2) m_5454048 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Lbpp$a;[J)V, bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Lbpp$a;[J)V

---

1) m_3590719 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Ljava/util/Map;)V, bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Ljava/util/Map;)V

**2) m_7734219 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Ljava/util/Map;)V**

--

**1) m_1530040 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Z)V**

2) m_2364727 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].a(Z)V, bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].a(Z)V


---

**1) m_7022151 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].b(J)V**

2) m_8864286 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].b(J)VV

---

**1) m_2618325 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].c()Ljava/util/Set;**

2) m_6261194 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].c()Ljava/util/Set;

---

1) m_2000539 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].f()Ljava/util/Set;

**2) m_5824327 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].f()Ljava/util/Set;**

---

**1) m_1340183 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].l()[Lit/unimi/dsi/fastutil/shorts/ShortList;**

2) m_1853948 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].l()[Lit/unimi/dsi/fastutil/shorts/ShortList;

---

1) m_1828948 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].p()Lbor;

**2) m_3636575 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].p()Lbor;**

---

**1) m_0972325 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].q()J**

2) m_2252476 <- bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].q()J*

---

**1) m_0874705 <- bpr<-bnw<-[java/lang/Object,bnv<-java/lang/Object].a(IILbnu;)V**

2) m_8884370 <- bpt<-bnw<-[java/lang/Object,bnv<-java/lang/Object].a(IILbnu;)V*

---

**1) m_1624950 <- boh<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].b(Ljava/util/Map;)V**

2) m_8908268 <- bnr<-[java/lang/Object,bmx<-[java/lang/Object,axk<-java/lang/Object]].b(Ljava/util/Map;)V, bop<-[java/lang/Object,bnu<-[java/lang/Object,bod<-[java/lang/Object,ayn<-java/lang/Object]]].b(Ljava/util/Map;)V

---

**1) m_4368911 <- fc<-[java/lang/Object,et<-[java/lang/Object,java/lang/Iterable]](itf).a(I)Ljava/lang/Object;**

2) m_4640952 <- xu<-[java/lang/Object,ey<-[java/lang/Object,java/lang/Iterable]].a(I)Ljava/lang/Object;

3) m_4949766 <- ez<-[java/lang/Object,ey<-[java/lang/Object,java/lang/Iterable]].a(I)Ljava/lang/Object;;

### 18w49a -> 18w50a

1) m_6112713 <- bok<-[boj<-[bnq<-java/lang/Object,afu<-[java/lang/Object,afi<-[java/lang/Object,afg<-java/lang/Object,afv<-java/lang/Object],afp<-[java/lang/Object,afv<-java/lang/Object]]],afw<-java/lang/Object].f()Ljd;

**2) m_7744478 <- agv<-[java/lang/Object,afv<-java/lang/Object,bz<-java/lang/Object].f()Ljd;**

---

1) m_5792722 <- apc<-[apu<-[ahl<-ahf<-ahe<-agv<-[java/lang/Object,afv<-java/lang/Object,bz<-java/lang/Object],apl<-[java/lang/Object,agu<-java/lang/Object]],apz<-java/lang/Object].dz()Z

**2) m_6447487 <- aqm<-apu<-[ahl<-ahf<-ahe<-agv<-[java/lang/Object,afv<-java/lang/Object,bz<-java/lang/Object],apl<-[java/lang/Object,agu<-java/lang/Object]].dz()Z**

3) m_8668866 <- aps<-[aqf<-apb<-asg<-apv<-apu<-[ahl<-ahf<-ahe<-agv<-[java/lang/Object,afv<-java/lang/Object,bz<-java/lang/Object],apl<-[java/lang/Object,agu<-java/lang/Object]],apz<-java/lang/Object].dz()Z*

---

**1) m_7783530 <- aqr<-[ags<-ahl<-ahf<-ahe<-agv<-[java/lang/Object,afv<-java/lang/Object,bz<-java/lang/Object],aho<-java/lang/Object,aqq<-[java/lang/Object,agu<-java/lang/Object],aqt<-java/lang/Object,bat<-java/lang/Object].dM()Laqs;**

2) m_9297159 <- aqn<-[aqm<-apu<-[ahl<-ahf<-ahe<-agv<-[java/lang/Object,afv<-java/lang/Object,bz<-java/lang/Object],apl<-[java/lang/Object,agu<-java/lang/Object]],aqt<-java/lang/Object].dM()Laqs;;

---

1) m_0092047 <- bnl<-bok<-[boj<-[bnq<-java/lang/Object,afu<-[java/lang/Object,afi<-[java/lang/Object,afg<-java/lang/Object,afv<-java/lang/Object],afp<-[java/lang/Object,afv<-java/lang/Object]]],afw<-java/lang/Object].a(Ljd;)V

**2) m_5513796 <- bok<-[boj<-[bnq<-java/lang/Object,afu<-[java/lang/Object,afi<-[java/lang/Object,afg<-java/lang/Object,afv<-java/lang/Object],afp<-[java/lang/Object,afv<-java/lang/Object]]],afw<-java/lang/Object].a(Ljd;)V**

---

1) m_1668060 <- cyu<-[cym<-czc<-java/lang/Object,dhw<-java/lang/Object,dje<-java/lang/Object].a()Lday;

**2) m_2824571 <- dam<-[cym<-czc<-java/lang/Object,dje<-java/lang/Object,dlf<-java/lang/Object].a()Lday;**

### 19w07a -> 19w08a

1) m_0251012 <- csf<-[crq<-java/lang/Object,css<-java/lang/Object,csv<-java/lang/Object].a(IIF)V

2) m_2774249 <- csd<-[crq<-java/lang/Object,css<-java/lang/Object,csv<-java/lang/Object].a(IIF)V

**3) m_3426670 <- cut<-[csg<-[crd<-java/lang/Object,csi<-[java/lang/Object,csh<-java/lang/Object]],ctw<-java/lang/Object].a(IIF)V, cvi<-[cst<-[crq<-java/lang/Object,csu<-[java/lang/Object,csw<-[java/lang/Object,csv<-java/lang/Object]]],css<-java/lang/Object,cuk<-java/lang/Object].a(IIF)V**

4) m_3816878 <- csa<-csg<-[crd<-java/lang/Object,csi<-[java/lang/Object,csh<-java/lang/Object]].a(IIF)V, csn<-[cst<-[crq<-java/lang/Object,csu<-[java/lang/Object,csw<-[java/lang/Object,csv<-java/lang/Object]]],css<-java/lang/Object].a(IIF)V

5) m_3842529 <- cxz<-[crq<-java/lang/Object,css<-java/lang/Object,csv<-java/lang/Object,cye<-java/lang/Object,qe<-java/lang/Object].a(IIF)V

6) m_7905474 <- crz<-[crq<-java/lang/Object,css<-java/lang/Object,csv<-java/lang/Object].a(IIF)V

7) m_9661580 <- cxy<-[crq<-java/lang/Object,css<-java/lang/Object,csv<-java/lang/Object].a(IIF)V


---

1) m_0734522 <- wn<-[java/lang/Object,wt<-java/lang/Object].a(Lvw;)V

**2) m_6560014 <- wx<-[java/lang/Object,wr<-[java/lang/Object,wt<-java/lang/Object]].a(Lvw;)V***

### 19w08b -> 19w09a

**1) m_1897788 <- asv<-[ahm<-[java/lang/Object,agl<-java/lang/Object,bz<-java/lang/Object],aso<-java/lang/Object].a(Lahm;FFFFF)V**

2) m_7517040 <- asd<-[ahm<-[java/lang/Object,agl<-java/lang/Object,bz<-java/lang/Object],aso<-java/lang/Object].a(Lahm;FFFFF)VV

### 1.14.4-pre3 -> 1.14.4-pre4

1) m_1482540 <- wc<-[java/lang/Object,nu<-[java/lang/Object,jh<-java/lang/Object]].a()Ljc;

**2) m_7400282 <- dkc<-[java/lang/Object,kf<-[java/lang/Object,jh<-java/lang/Object]].a()Ljc;**;
