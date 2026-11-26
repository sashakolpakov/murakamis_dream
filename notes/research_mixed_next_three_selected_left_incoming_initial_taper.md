# The initial incoming path and its taper on the selected left contour

Private proof candidate, 8 November 2026. The complete initial real
incoming interval and its original taper satisfy an exponential upper
bound after the shared variable is moved to height \(1/100\). The proof
retains every finite row and every term of the contour identity.
It does not estimate the incoming corner or the middle Fourier sum.
No mathematical numerical evaluation is used.

## 1. Source and statement

Use an actual complete word in powers three and four beginning \(343\),
of length at least five, with the coupled reference and notation of
[the actual initial and taper theorem](research_mixed_next_three_actual_incoming_initial_taper.md).
Write
\[
 (a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3),\qquad
 h_a=\Im a_*,\quad h_s=\Im s_*,\quad h_t=\Im t_*,\quad h_z=\Im z_*.
\]
In particular
\[
 -.072<h_a<0,\quad -.102<h_s<-.001,\quad
 -.03<h_t,h_z<.02.
 \tag{1}
\]
Keep the same cap supporting plane \(B_U\), final affine rate
\(\Lambda_{123}\), action \(\mathcal P_0^+\), and original logarithmic
lifts. Put
\[
 \begin{gathered}
 H=1/100,\quad y=q+iH,\quad 0\le q\le11/50,\qquad
 z=u+ih_z,\quad 3/10\le u\le39/100,\\
 Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz},\quad
 R=|Y|=e^{\pi/50}<16/15,\qquad B_f=77/50+\pi/50.
 \end{gathered}
 \tag{2}
\]
The outgoing real interval contains the actual third reference
coordinate. The two positively oriented incoming paths are
\[
 \Gamma_{\rm in}=[0,1/10],\qquad
 \Gamma_{\rm tap}:\ a(x)=x-i\lambda(x-1/10),\
 1/10\le x\le11/50,\qquad
 \lambda=-h_a/(3/25)\in(0,3/5).
 \tag{3}
\]
The endpoint of the taper is \(a_0=11/50+ih_a\).

Retain the literal finite functions
\[
 \begin{split}
 &D=N-1,\quad r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 p_j(V)=(rV;r)_j,\\
 &U_{0,N}(w,X)=\sum_{j=0}^{D}H_N(w,r^{-j})p_j(X)/P_j,\\
 &C_{\beta,N}(V,W)=\sum_{j=0}^{D}
        V^{-j}p_j(V)p_j(W)/P_j^{2+\beta},\qquad X=e^{-2\pi ia}.
 \end{split}
 \tag{4}
\]
Here \(H_N\) is the original coherent cap coefficient. The entire
polynomial \(d_N\), of degree at most \(D\), has
\(d_N(r^b)=P_b^{-1}\). Define
\[
 \mathcal D_N(a;y,z)=
 U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)Y^{-N}C_{0,N}(Y,Z).
 \tag{5}
\]
There is no outgoing halfweight for the next type-three factor.

**Theorem.** For all real ordinary colors \(w\in[-2,2]\), both level
parities, and all sufficiently large \(N\),
\[
 |\mathcal D_N(a;y,z)|
 \le CN^B e^{N\{\Lambda_{123}(z)-1/10000\}},
 \qquad a\in\Gamma_{\rm in}\cup\Gamma_{\rm tap}.
 \tag{6}
\]
The same exponential rate bounds either original integral
\(N\int_{\Gamma}\mathcal D_N\,da\). This theorem makes no new
outside-parameter derivative claim.

## 2. The endpoint comparisons that will be transported

Use the original primitive
\(g(\xi)=(\operatorname{Li}_2(e^{-2\pi i\xi})-\pi^2/6)/(2\pi i)\)
on its prescribed lift, so \(g'(\xi)=\operatorname{Log}(1-e^{-2\pi i\xi})\).
For real \(t\), write
\(J(t)=\int_0^t\log(2|\sin\pi s|)\,ds\).
For the bare phases use
\[
 Q_\beta(v;b,c)=g(b+v)+g(c+v)-(2+\beta)g(v)-g(b)-g(c)+2\pi ibv.
 \tag{7}
\]
The two selected Fourier rates are
\[
 W_{\rm fac}(y)=-\Re g(y)-2\pi H,\qquad W_{\rm force}(y)=0.
 \tag{8}
\]
The profile proofs in
[central selected-left completion](research_mixed_next_three_selected_left_central_completion.md),
Sections 2--4, supply at \(a=a_0\) a reserve greater than \(1/125\)
for each first main profile \(s=v+ih_s,\ 1/8\le v\le1/2\), the
real cuts \(s=1/8,1/2\), and the first last profile
\[
                    -2\pi h_a+2\pi H.
 \tag{9}
\]
Each of these comparisons includes \(B_U(11/50)\), either rate in
(8), and every next controlling profile. The next physical upper
rows are included by that proof's separate upper-row comparisons.
The complete next currents reduce to the same profiles. These are
individual rate comparisons before either conditional sum is taken.

The original cap envelope on the taper consists of regular profiles
\(\Psi_0(e,a)\), with
\[
 e=u_e+ik,\qquad 27/100\le u_e\le49/100,\qquad
 -19/1000\le k\le37/1000,
 \tag{10}
\]
and its separate true-end alternative. All these profiles are bounded
by \(B_U(11/50)\) at \(a_0\). The cap's own contour terms have already
been reduced to this envelope, with their original coefficients.
This is the source statement in Sections 2 and 7 of
[the original left taper](research_mixed_next_unselected_incoming_left_taper.md),
with its all-real-color extension.

The other input is the complete attachment estimate from
[selected-left filter correction](research_mixed_next_three_selected_left_filter_correction.md).
Any preceding factor independent of the next private index and bounded
by \(CN^B e^{NB_f}\) can be multiplied by the entire
\(d_N(Y)Y^{-N}C_{0,N}(Y,Z)\), with finite gap \(1/2000\)
below \(\Lambda_{123}(z)\). We use this only after proving the
required preceding-factor bound.

## 3. Low rows and main profiles on the taper

Keep the moving real cut
\[
 \ell(x)=7/100+x/4,\qquad
 \ell(1/10)=19/200,\quad \ell(11/50)=1/8.
 \tag{11}
\]
For fixed real index \(v\), the incoming derivative of a cap profile
coupled to the first conditional profile is
\[
 \frac d{dx}\Re\{\Psi_0(e,a(x))+Q_1(v;a(x),y)\}
 =\Re D_a+\lambda\Im D_a,\quad
 D_a=g'(e+a)+g'(a+v)-2g'(a)+2\pi iv.
 \tag{12}
\]
It is independent of \(y\). Thus the two derivative bounds
\(-118/875\) and \(-139/800\) from Section 2 of
[the lower-left initial/taper proof](research_mixed_next_lower_left_incoming_initial_taper.md)
remain valid on its two \(x\)-intervals.

The force at a real index is
\[
 e^{\Re Q_{1,s}(v;a,y)}
 =\frac{|T-e^{-2\pi i(x+v)}|\,|1-Re^{-2\pi i(q+v)}|}
              {(2\sin\pi v)^3},\qquad T=e^{-2\pi\Im a}\ge1.
 \tag{13}
\]
The old force estimates \(9/5\) and \(135/64\) used only a minimum
over nonnegative outgoing radii, not the inequality \(R\le1\).
They therefore remain valid at (2). Together with \(\ell'=1/4\)
they give the same moving-cut derivative greater than \(1/200\).
The separate true-cap-end profile has the same increasing transport.
Every low physical row increases to this real cut: the two numerator
bounds in that proof give force at least
\(\cos(\pi v)/(2\sin\pi v)>1\), for \(0<v\le\ell(x)\).
The exact zero row is retained.

There is one radius restriction in the old main-index clipping that
does require a new argument. Write
\[
 \rho=e^{2\pi h_s}\in(1/2,1),\qquad
 D_0=|1-\rho e^{-2\pi iv}|^2,\qquad
 \ell(x)\le v\le3/20.
 \tag{14}
\]
The incoming modulus is greater than \(15/16\), and
\(D_0<1+\rho^2-7\rho/6\le5/6\), exactly as in that proof.
Minimizing the outgoing modulus over all its radii gives
\[
              |1-\rho R e^{-2\pi i(q+v)}|\ge\sin(2\pi v).
 \tag{15}
\]
Indeed \(q+v\in[v,.37]\): below \(1/4\) the minimized sine
increases, and above \(1/4\) the radial minimum is one.

If \(\rho\ge2/3\), then
\[
 4\sin^2(\pi v)>1/3\ge1-\rho,\qquad
 \sin^2(2\pi v)-D_0\cos^2(\pi v)
  =(1-\rho)\cos^2(\pi v)\{4\sin^2(\pi v)-(1-\rho)\}\ge0.
 \tag{16}
\]
For the first strict inequality, \(\pi>25/8\) and the sine cubic give
\(\sin(19\pi/200)>\sin(19/64)>7/24\);
\(4(7/24)^2>1/3\). Also \(\cos(\pi v)>8/9\).
Thus the main force exceeds
\((15/16)(8/9)/D_0>1\).

For \(1/2<\rho\le2/3\) and \(v\le1/8\), one has
\[
 D_0<1+\rho^2-7\rho/5\le11/20,\qquad
 \sqrt{D_0}<3/4,\qquad \sin(2\pi v)>11/20.
 \tag{17}
\]
The numerator product is greater than \(165/320\), whereas
\(D_0^{3/2}<33/80\). For \(1/8\le v\le3/20\), instead
\[
 D_0<2/3,\qquad \sqrt{D_0}<5/6,\qquad
 \sin(2\pi v)>7/10.
 \tag{18}
\]
The numerator product exceeds \(21/32>5/9>D_0^{3/2}\).
This proves increasing main-index transport to \(3/20+ih_s\)
in all cases, without \(R\le1\).

On the rest of the first main segment and on the real half cut,
the original incoming transport is unchanged, since (12) is
independent of the shared variable. It reaches \(a_0\), where
Section 2 applies. The next profiles and their weights are constant
throughout this incoming transport.

## 4. All first conditional contour terms

Use the same private heights \(-1/5,+4\), main height \(h_s\),
and real cuts \(\ell(x),1/2\). For
\(19/200\le v\le1/2\), put \(J_1(v,\sigma)=\Im Q_{1,s}(v+i\sigma;a,y)\).
The bounds required here are
\[
 -21\pi/20<J_1(v,\sigma)<11\pi/10\quad(\sigma\le0),\qquad
 J_1(v,\sigma)>-19\pi/10\quad(\sigma\ge0).
 \tag{19}
\]
Here is the change from the old proof. For \(\sigma\le-H\),
both shifted outer heights are nonpositive and its original
four-case bounds apply. For \(-H\le\sigma\le0\), only the outgoing
argument changes. At a shifted real coordinate
\(b=q+v\in[19/200,18/25]\), its excess over the height-zero argument is
\[
 \arctan\{\tanh(\pi(H+\sigma))\cot(\pi b)\}.
 \tag{20}
\]
Its absolute value is less than \(7\pi/200\), since
\(|\cot(\pi b)|<7/2\). Adding this to the old bounds
\(-203\pi/200,103\pi/100\) proves the first two inequalities
in (19). For \(0\le\sigma\le.12\), the old lower argument bound
used only the all-height lower bounds for both shifted arguments,
so is unchanged. For \(\sigma\ge.12\), both shifted heights are
positive, as required in its remaining four cases. This proves
the final inequality in (19).

The lower horizontal alias therefore loses at least \(9\pi/50\)
relative to the same main profile. The upper alias loses more than
\[
 \pi\{8-(19/10)4-(21/20)(51/500)\}
                       =2929\pi/10000>\pi/4.
 \tag{21}
\]
The four weighted sides decrease away from their real endpoints,
by (19).

Both unweighted joins also remain bounded by their real and main
endpoints. To check the changed outgoing height explicitly, set
\[
 C(v,\sigma)=\Re\cot\pi(v+i\sigma)
 =\frac{\sin(2\pi v)}{\cosh(2\pi\sigma)-\cos(2\pi v)}.
 \tag{22}
\]
For \(19/200\le v<1/2\) and any real \(\sigma\),
\[
                   C(v,\sigma+H)<\frac65 C(v,\sigma).
 \tag{23}
\]
Write \(c=\cos(2\pi v)<5/6\), \(z=2\pi\sigma\), \(h=2\pi H\).
The desired denominator inequality is
\[
 5\cosh z-6\cosh(z+h)+c<0.
 \tag{24}
\]
Its left side is at most
\(-\sqrt{61-60\cosh h}+c\).
The positive series gives \(\cosh h<\cosh(1/15)<401/400\);
thus the square root exceeds \(\sqrt{17/20}>5/6\).
This proves (23).

On the low strip \(19/200\le v\le1/8\), the old angle-maximum
comparison at fixed height bounds a positive outgoing cotangent
by \(12/11\) times the one at the unshifted angle. This comparison
requires only \(\cosh(2\pi(\sigma+H))<5/4\), which holds for
\(h_s\le\sigma\le0\). Combining it with (23) gives
\[
 C(q+v,\sigma+H)\le\frac{72}{55}C(v,\sigma)
 \quad\hbox{whenever the left side is positive}.
 \tag{25}
\]
The own cotangent exceeds one, while the incoming shifted cotangent
is less than \(3/2\), by the original low-strip proof. Hence
\[
 3C(v,\sigma)-C(x+v,\Im a+\sigma)-C(q+v,H+\sigma)
                         >\frac{93}{55}-\frac32=\frac{21}{110}>0.
 \tag{26}
\]
For \(1/8\le v<1/2\), the fixed-height cotangent decreases in
its positive real range, because
\(\cosh(2\pi\sigma)\cos(2\pi v)<1\). The incoming positive
cotangent is at most the own one, and the outgoing one is at most
\(6/5\) times it by (23). This again proves positive vertical
curvature. At the half cut the shifted incoming cotangent is
strictly negative, and the outgoing one is nonpositive.
Thus the two unweighted joins are covered as well.

The exact cotangent decomposition keeps its \(+N\) main measure,
two horizontal aliases, four weighted sides, and two unweighted
joins. Equations (19)--(26) control every one of these terms by
the main and real-cut profiles transported in Section 3.

## 5. Every upper physical row

Let \(E_1(t;a,y)\) be the literal physical row rate, and
\(\delta_a=-2\pi\Im a\ge0\). Its full last rate at the selected
height is \(\delta_a+2\pi H\). Reflection gives
\[
 \begin{split}
 \Phi(v)&=E_1(1-v;a,y)-\delta_a-2\pi H\\
 &=3J(v)
 -\int_0^v\log|T-e^{-2\pi i(x-s)}|\,ds
 -\int_0^v\log|1-Re^{-2\pi i(q-s)}|\,ds ,
 \qquad 0\le v\le1/2.
 \end{split}
 \tag{27}
\]
This retains the incoming carrier and the outgoing mean \(\log R\).

On both incoming paths, the original radius-position comparison
in Section 4 of the lower-left initial/taper proof bounds the
incoming modulus in the complementary integrals by \(21/10\),
with logarithm less than \(3/4\). The outgoing modulus is at most
\(31/15\), whose logarithm is less than \(73/100\). The latter
inequality follows by retaining terms through degree four in
the positive series for \(e^{73/100}\). Therefore
\[
 \Phi(v)-\Phi(1/2)
                \le\frac{37}{25}(1/2-v)+3J(v).
 \tag{28}
\]

We need a slightly sharper written bound for \(J(9/50)\) than
the one used at negative shared height. The alternating series
for Catalan's constant gives
\[
 \begin{split}
 G_{\rm Cat}
 &>1-\frac19+\frac1{25}-\frac1{49}
       +\frac1{81}-\frac1{121}
       +\frac1{169}-\frac1{225}
       +\frac1{289}-\frac1{361}\\
 &>\frac{88888+1959+408+147+69}{100000}
   =\frac{91471}{100000}.
 \end{split}
 \tag{29}
\]
The five lower bounds follow by grouping adjacent positive-minus-negative
terms and cross-multiplying integers. Consequently
\[
 -J(1/4)=\frac{G_{\rm Cat}}{2\pi}
 >\frac{640297}{4400000}>\frac{291}{2000}.
 \tag{30}
\]
The original concave-log chord bound on \([9/50,1/4]\) contributes
more than \(13/1000\). Explicitly its lower bound is
\((7/200)(2/41+1/3)>13/1000\). Thus
\[
                         -J(9/50)>\frac{317}{2000}.
 \tag{31}
\]
The right side of (28) is convex on \([9/50,1/2]\), vanishes
at \(1/2\), and at \(9/50\) is less than
\[
                   \frac{296}{625}-\frac{951}{2000}
                                  =-\frac{19}{10000}.
 \tag{32}
\]
Every upper row with reflected index \(v\ge9/50\) is therefore
bounded by its real-half profile, which is already transported.

If \(v\le9/50\) and \(x\ge9/50\), the incoming arc is in
\([0,1/2]\) and contributes at least \(J(v)\). The outgoing
arc contributes at least \(2J(v/2)\), since \(R\ge1\) increases
every modulus above its unit-radius chord. Hence
\[
                  \Phi(v)\le2\{J(v)-J(v/2)\}\le0.
 \tag{33}
\]
It remains to transport the cap plus this literal last profile.
For a regular cap profile (10), let
\[
 D_{\rm cap}=g'(e+a)-g'(a).
 \tag{34}
\]
On the taper \(x\in[.18,.22]\), its real part is positive.
Indeed put \(r_a=e^{2\pi\Im a}\le1\),
\(r_e=e^{2\pi k}>7/8\). On the larger interval
\(.1\le x\le.22\), one has
\(\cos(2\pi x)>9/50\) and
\(\cos(2\pi(x+u_e))<-1/5\). Subtracting the two squared
moduli in the ratio defining (34) gives more than
\[
 r_a\left\{-\frac{15}{64}r_a+
                 2\left(\frac9{50}+\frac7{40}\right)\right\}
                           \ge\frac{761}{1600}r_a>0.
 \tag{35}
\]
The radius bound follows, for example, from
\(e^{-19\pi/500}>1-19\pi/500>7/8\).
The shifted argument is at least \(-21\pi/50\), while the
incoming argument is at most \(2\pi/5\). Thus
\[
 \frac d{dx}\{\Re\Psi_0(e,a(x))+\delta_a+2\pi H\}
 =\Re D_{\rm cap}+\lambda(\Im D_{\rm cap}+2\pi)>0.
 \tag{36}
\]
The true-cap-end envelope is constant on these nonpositive heights,
apart from the increasing carrier \(\delta_a\). It has the same
nondecreasing transport. Every cap-plus-last profile reaches the
paid endpoint (9). This use of individual cap profiles does not
extract them from a bound on the coherent cap.

For the final case \(v\le9/50,\ x\le9/50\), both arcs have their
centered lower bounds, so
\[
 \Phi(v)\le3J(v)-4J(v/2)
 \le v\{\log(8\pi v)-1\}+\pi^2v^3/30
 <\frac{101}{1000}.
 \tag{37}
\]
This is the original integrated-log inequality with a sharper
logarithmic witness. Namely
\(\log(36\pi/25)<31/20\), since the positive exponential
series through degree four at \(31/20\) exceeds \(23/5>792/175\).
The first term in (37) is convex, so its maximum on this interval
is bounded by its endpoint values. Using \(\pi^2<10\), the total
is at most
\[
                   \frac{99}{1000}+\frac{243}{125000}
                         =\frac{12618}{125000}<\frac{101}{1000}.
 \tag{38}
\]
The complete cap has its original unit-disk rate
\(101/125+13/40\), and \(\delta_a\le12\pi/125\) when
\(x\le9/50\) on the taper; it is zero on the initial real path.
Hence the cap times this entire positive upper-row group has rate
strictly below
\[
 \frac{101}{125}+\frac{13}{40}+\frac{12\pi}{125}
       +\frac{101}{1000}+\frac{\pi}{50}
 <\frac{43}{28}+\frac{\pi}{50}
 =B_f-\frac3{700}.
 \tag{39}
\]
The complete bounded-factor attachment in Section 2 applies.
The original uniform zero-safe numerator and factorial bounds include
both true ends and both parities. Choose their tolerances inside
the explicit reserve in (39). No physical row is deleted.

## 6. The remaining initial real interval

The interval \([0,1/32]\) is already covered by
[the incoming-end theorem](research_mixed_next_three_selected_left_incoming_ends.md),
with gap \(1/2000\). On \([1/32,1/10]\), keep the cap's original
complete regular envelope, its extra real profiles
\(49/100\le e\le1/2\), and its separate true ends.
Use the fixed first real cut \(19/200\).

For every conditional current point \(s=v+i\sigma\), the original
incoming derivative on this real path is
\[
 \frac d{dx}\Re\{\Psi_0(e,x)+Q_1(v+i\sigma;x,y)\}
 =\log\frac{|1-e^{-2\pi i(e+x)}|
                  |e^{-2\pi\sigma}-e^{-2\pi i(x+v)}|}
                  {(2\sin\pi x)^2}>\log(11/8).
 \tag{40}
\]
It is independent of \(y\); every alias penalty and following
factor is independent of \(x\). Thus all these profiles transport
to \(x=1/10\), where Sections 3--4 apply. The extra cap real
profiles clip to \(e=49/100\) there, by the original cap proof.
The physical low rows still increase to their real cut, and all
physical upper rows are covered in Section 5.

The cap's separate true-end layers, coupled to the complete first
conditional factor, have unit-disk rate \(389/300\), by Section 5
of the lower-left initial/taper source. Their outgoing degree is
at most \(D\). The reciprocal-polynomial maximum principle therefore
adds at most \(\pi/50\) on the present circle. Since
\(389/300<77/50\), the complete bounded-factor attachment applies
to these terms as well.

## 7. Finite assembly and the positive-height endpoint

First work on a fixed compact interval
\(\epsilon\le q\le11/50\). Set the exact private half-grid cuts
using
\[
 L_N=\lfloor N\ell(x)\rfloor+1,\qquad
 M_N=\lceil N/2\rceil,\qquad
 \ell_N=(L_N-1/2)/N,\qquad b_N=(M_N-1/2)/N.
 \tag{41}
\]
On the initial path take \(\ell=19/200\). Keep all low rows
\(j<L_N\), middle rows \(L_N\le j<M_N\), and upper rows
\(M_N\le j<N\).
The first middle sum has the literal canonical interpolant
\[
 e^{2\pi iNas}
 \frac{\Pi_N(a+s)\Pi_N(y+s)}
      {\Pi_N(a)\Pi_N(y)\Pi_N(s)^3}.
 \tag{42}
\]
Its exact cotangent identity keeps the main measure \(+N\,ds\),
both horizontal aliases, four weighted vertical terms and two
unweighted joins. Sections 3--6 bound every term. At jumps of the
moving integer cut both adjacent partitions have the same bounds.
The \(O(N^{-1})\) cut displacements cost arbitrarily small
uniform rate tolerances.

The next kernel and the whole forced Fourier polynomial retain
all the terms of their adopted selected-left estimates. Their
comparison is performed with the first cap profile or bounded
preceding group still attached. The raw groups have gap \(1/2000\);
the transported profiles have reserve greater than \(1/125\).
After choosing the total finite tolerances inside these reserves,
one obtains gap at least \(1/4000\) for the complete product on
this compact interval.

To include \(q=0\), use the complete finite expression (5).
Its Laurent support in \(Y\) is contained in
\[
                       [-D-N,\,2D-N].
 \tag{43}
\]
This follows directly from the outgoing degree \(D\) of the first
kernel, degree \(D\) of \(d_N\), and incoming band \([-D,0]\)
of the next kernel. All frequencies have modulus less than \(2N\).
The fixed short-arc continuation used in the central selected-left
proof extends the complete bound across \(q=0\), with rate loss
less than \(1/20000\), by first choosing its arc and ellipse
and then choosing \(\epsilon\) inside the resulting extension width.
No asymptotic symbol at the positive-height factorial seam is used.
The remaining gap exceeds \(1/10000\), proving (6).

Finally the two original measures are \(+N\,dx\) and
\(+N(1-i\lambda)\,dx\). Their bounded lengths and factors change
only the polynomial prefactor. This proves the integral assertion.
The central and right incoming paths, the oriented corner, the
remaining shared-variable contours, and the full observed Fourier
sum keep their separate obligations.
