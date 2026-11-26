# The complete conditional polynomial at the incoming half face

Research deduction, 7 November 2026. The literal conditional source
\(C_{1,N}(-1,Y)\) has a nonzero, uniform asymptotic expansion on the
whole selected outgoing interval. This includes every physical row,
both parities, both horizontal residue remainders, both full vertical
remainders, and the connectors of the main integral.

The result concerns the conditional factor alone. The complete cap
\(U_{0,N}(w,-1)\), its private cut currents, and comparison of their
product with the actual next-source affine action remain separate.
No numerical evaluation or certificate replay is used.

## 1. The literal source and original critical sheet

Keep
\[
 \begin{gathered}
 r=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad p_j(X)=(rX;r)_j,\\
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                  \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\\
 a=\frac12,\qquad y=x+iH,\qquad
 \mathcal Y=\left\{\frac{11}{50}\le x\le\frac9{20},
                                     \quad0\le H\le\frac1{100}\right\},
 \qquad Y=e^{-2\pi iy}.
 \end{gathered}                                                    \tag{1}
\]
These are the exact conventions of
[the conditional torus source](research_mixed_conditional_torus_composition.md).
Use the original primitive
\[
 g(z)=J(z)+\frac{\pi i}{2}(z-z^2),\qquad
 g'(z)=\Log(1-e^{-2\pi iz}),\qquad
 g''(z)=\pi(\cot\pi z-i)
                                                               \tag{2}
\]
on \(0<\Re z<1\). The logarithm in (2) is principal. The full
unmarked row phase is
\[
 Q(t;y)=g(t+\tfrac12)+g(t+y)-3g(t)
                         -g(\tfrac12)-g(y)+\pi it.
                                                               \tag{3}
\]
In particular the two outer factorial divisions are retained.

Put \(T=e^{-2\pi it}\) and \(\omega=T^{-1}\). Direct exponentiation,
including the chirp \(\pi i\) in \(Q_t\), gives
\[
 e^{Q_t}
   =-\frac{(1+T)(1-TY)}{(1-T)^3}.
                                                               \tag{4}
\]
The critical equation is therefore
\[
 \begin{split}
 &T^3+(Y-3)T^2+(Y+2)T-2=0,\\
 &2\omega^3-(2+Y)\omega^2+(3-Y)\omega-1=0,\\
 &Y=\frac{2\omega^3-2\omega^2+3\omega-1}{\omega(\omega+1)}
       =2\omega-4-\omega^{-1}+\frac8{\omega+1}.
 \end{split}                                                    \tag{5}
\]

**Lemma 1.** For every \(\Im Y<0\), the cubic in (5) has exactly
one root in \(\Im\omega>0\), counting multiplicity. This root is
simple and defines a holomorphic function \(\omega(Y)\).
For
\[
 t(Y)=\frac{\Log\omega(Y)}{2\pi i},\qquad
 y(Y)=-\frac{\Log Y}{2\pi i},
                                                               \tag{6}
\]
with arguments respectively in \((0,\pi)\) and \((-\pi,0)\),
the exact original equation is \(Q_t(t(Y);y(Y))=0\).

*Proof.* Neither \(0\) nor \(-1\) is a root of the cubic.
By the rational equation in (5), a real root would make \(Y\)
real. Thus no root crosses the real axis as \(Y\) varies in the
lower half-plane. The leading coefficient is the constant \(2\),
so roots do not escape to infinity on compact parameter paths.
The upper-half-plane root count is consequently constant.

At \(Y=-i\), the factorization is
\[
 (\omega-i)\{2\omega^2+(-2+3i)\omega-i\}.
                                                               \tag{7}
\]
The two quadratic roots are
\((2-3i\pm\sqrt{-5-4i})/4\).
Writing the square root as \(u-iv\), \(v>0\), gives
\(v^2=(\sqrt{41}+5)/2<6<9\). Both quadratic roots therefore
have negative imaginary part. There is exactly one upper root,
with multiplicity one. Local implicit functions glue to the
stated global root.

Equations (6) give \(0<\Re t,\Re y<1/2\).
Hence \(t,t+1/2,t+y,y\) all lie in the original regular strip.
The original \(Q_t\) is holomorphic on this sheet and has
exponential equal to one. At \(Y=-i\), \(t=y=1/4\), its value
is zero directly from (2). Its integer logarithmic lift is
therefore zero throughout the connected lower half-plane.
\(\square\)

## 2. A uniform source-chart enclosure

On (1),
\[
 1\le |Y|\le e^{\pi/50}<\frac{175}{164}<\frac87,\qquad
                  \Im Y<0,\quad \Re Y>-\frac87.
                                                               \tag{8}
\]
The exponential estimate follows from
\(\pi<22/7\) and \(e^u<(1-u)^{-1}\).
Write \(\omega=\sigma+i\tau\), \(\tau>0\), \(s=|\omega|^2\),
and \(D=|\omega+1|^2=s+2\sigma+1\). Equation (5) gives
\[
 \begin{split}
 \Im Y&=\tau\left(2+s^{-1}-8/D\right)<0,\\
 \Re Y&=\sigma(2-s^{-1})-4+\frac{8(\sigma+1)}D,\qquad
                    D<\frac{8s}{2s+1}.
 \end{split}                                                    \tag{9}
\]

If \(|\omega|\ge2\), then \(s\ge4\) and
\(\sigma<(3-s)/2\le-1/2\), because the upper bound for \(D\)
in (9) is less than four. When \(\sigma\le-1\), (9) gives
\(\Re Y<-4\). When \(-1<\sigma<-1/2\), one has
\(D>s-1\ge3\), so the last term in (9) is less than \(4/3\);
the first term is negative. Thus \(\Re Y<-8/3\).
Both cases contradict (8).

If \(|\omega|\le1/2\), put
\[
 h(s)=\frac{-2s^2+5s-1}{2(2s+1)},\qquad 0<s\le1/4.
\]
The last inequality in (9) says \(\sigma<h(s)\).
For fixed \(s\), the real expression in (9) has derivative
\[
 2-s^{-1}+\frac{8(s-1)}{(s+2\sigma+1)^2}<0.
                                                               \tag{10}
\]
Its value at \(h(s)\) is
\[
 \frac{-4s^3+6s^2-2s+1}{s(2s+1)}>2,
                                                               \tag{11}
\]
because the numerator after subtracting \(2s(2s+1)\) is
\(1-4s+2s^2(1-2s)>0\). Hence \(\Re Y>2\), again contradicting
(8). We have proved \(1/2<|\omega|<2\).

There is also a fixed lower real-part bound. If
\(\sigma\ge9|\omega|/10\), writing \(r_0=|\omega|>0\) gives
\[
 \begin{split}
 (2s+1)D-8s
 &\ge 2r_0^4+\frac{18}{5}r_0^3-5r_0^2
                                  +\frac95r_0+1>0 .
 \end{split}                                                    \tag{12}
\]
Indeed the sum of the cubic and linear terms is at least
\((18\sqrt2/5)r_0^2>5r_0^2\); the latter inequality follows
by squaring, since \(648>625\). This contradicts (9).
Thus \(\cos\arg\omega<9/10<\cos(\pi/8)\). It follows that
\[
 \boxed{\quad
 \frac1{16}<\Re t(y)<\frac12,\qquad
 |\Im t(y)|<\frac{\log2}{2\pi}<\frac3{25}
                       \quad(y\in\mathcal Y).\quad}
                                                               \tag{13}
\]
For the final inequality use \(\log2<7/10\) and \(\pi>3\).
The selected parameter set is compact, so the distances of the
critical point from both real endpoints in (13) have positive
uniform minima. No extension of a physical-index asymptotic was
used to produce this sheet.

## 3. Strict horizontal curvature in the full main strip

For \(C(z)=\Re\cot\pi z\), the exact second derivative is
\[
 \pi^{-1}\Re Q_{tt}(t;y)
       =C(t+\tfrac12)+C(t+y)-3C(t).
                                                               \tag{14}
\]

**Lemma 2.** Uniformly for \(y\in\mathcal Y\),
\[
 -\Re Q_{tt}(v+ih;y)>\frac{3\pi}{25}
 \quad\left(\frac1{20}\le v<\frac12,\quad |h|\le\frac3{25}\right).
                                                               \tag{15}
\]

*Proof.* Use
\[
 C(v+ih)=\frac{\sin2\pi v}{\cosh2\pi h-\cos2\pi v}.
                                                               \tag{16}
\]
Here \(C(t+1/2)<0\) and \(C(t)>0\). The elementary bounds needed
below are
\[
 \cosh(6\pi/25)<4/3,\quad \cosh(13\pi/50)<3/2,\quad
 \sin(\pi/10)>3/10,\quad \cos(14\pi/25)>-1/5.
                                                               \tag{17}
\]
For completeness, the even power series implies
\(\cosh z\le1+z^2/[2(1-z^2/12)]\) for \(z^2<12\).
Apply it with \(6\pi/25<19/25\) and
\(13\pi/50<41/50\); the respective rational comparisons are
\(19\cdot361<12\cdot625\) and
\(13\cdot1681<12\cdot2500\).
Also \(\pi>25/8\) and \(\sin u\ge u-u^3/6\) give
\(\sin(\pi/10)>\sin(5/16)>3/10\).
Finally \(\cos(14\pi/25)=-\sin(3\pi/50)>-1/5\).

For \(1/20\le v\le1/8\), (16)--(17) give \(C(t)>9/19\).
For \(1/8\le v\le7/25\), they give \(C(t)>21/46\):
the numerator exceeds \(7/10\), and the denominator is less than
\(4/3+1/5=23/15\).
If \(v+x<1/2\), then
\(C(t+y)\le\cot\pi(v+x)<1\), since \(v+x\ge27/100\);
if \(v+x\ge1/2\), this term is nonpositive.
Thus these first two intervals give
\(-\Re Q_{tt}>17\pi/46>3\pi/25\).

For \(7/25\le v\le2/5\), the shifted term is nonpositive,
whereas \(C(t)>3/14\): its numerator exceeds \(1/2\) and its
denominator is less than \(7/3\). This gives
\(-\Re Q_{tt}>9\pi/14\).

For \(2/5\le v<1/2\), the shifted real part lies in
\([31/50,19/20)\) and its height has modulus at most \(13/100\).
Its sine numerator is less than \(-3/10\) and its positive
denominator is less than \(5/2\). Thus \(C(t+y)<-3/25\).
The other two terms in (14) are favorable, proving (15).
\(\square\)

Consequently the horizontal phase through \(t(y)\) has its
unique maximum at that point. The real phase on every vertical
segment in this strip is strictly convex, since
\(\partial_h^2\Re Q=-\Re Q_{tt}\).
This convexity assertion is only used for \(|h|\le3/25\).
The long residue sides at heights up to two use different
argument estimates in Section 5.

## 4. An action floor with no root evaluation

Define the holomorphic critical action
\[
 \Theta(y)=Q(t(y);y),\qquad M_1(y)=\Re\Theta(y).
                                                               \tag{18}
\]

**Lemma 3.** On \(\mathcal Y\), \(M_1(y)>13/24\).

*Proof.* Put \(c=-J(1/4)\). The alternating Catalan-series
bound, as written in
[the fixed-cut obstruction, equations (11)--(12)](research_mixed_next_half_face_fixed_cut_obstruction.md),
gives \(c>14/99\).
At the real trial \(t_0=1/4\), the incoming numerator contributes
\(J(3/4)-J(1/2)=c\), and the three denominator factorials
contribute \(3c\). The chirp \(\pi it_0\) has zero real part.
The outgoing contribution is the exact integral
\[
 \Re\{g(y+\tfrac14)-g(y)\}
   =\int_0^{1/4}\log|1-e^{2\pi H-2\pi i(x+s)}|\,ds.
                                                               \tag{19}
\]
Here \(x+s\in[11/50,7/10]\). Increasing a radius from one
increases each modulus in (19). On this arc,
\[
 2\sin\pi(x+s)\ge2\sin(11\pi/50)>5/4.
                                                               \tag{20}
\]
Indeed \(\pi>25/8\) gives
\(\sin(11\pi/50)>\sin(11/16)
 \ge15565/24576>5/8\); the other end of the arc has larger sine.
Using \(\log(5/4)>2/9\), we obtain
\[
              \Re Q(1/4;y)>56/99+1/18=41/66.
                                                               \tag{21}
\]
The logarithm bound is the elementary inequality
\(\log u>2(u-1)/(u+1)\), \(u>1\).

At this trial the original own-argument terms and the chirp
cancel in the imaginary derivative:
\[
 \Im Q_t(1/4;y)=\arg(1-e^{-2\pi i(y+1/4)}).
                                                               \tag{22}
\]
At radius one its absolute value is at most \(\pi/5\), because
\(x+1/4\in[47/100,7/10]\). The doubled-angle cosine on this
interval is nonpositive. The absolute derivative of the
argument with respect to logarithmic radius is at most
\(R/(1+R^2)\le1/2\). Since \(\log R\le\pi/50\),
\[
                         |\Im Q_t(1/4;y)|\le21\pi/100.
                                                               \tag{23}
\]
Put \(h_*=\Im t(y)\). Vertical convexity from Lemma 2 gives
\[
 \begin{split}
 \Re Q(1/4+ih_*;y)
 &\ge\Re Q(1/4;y)-|h_*|\,|\Im Q_t(1/4;y)|\\
 &>\frac{41}{66}-\frac{21}{200}\log2
  >\frac{41}{66}-\frac{147}{2000}>\frac{13}{24}.
 \end{split}                                                    \tag{24}
\]
For the final rational comparison,
\(41/66-13/24=7/88\) and
\(7\cdot2000-147\cdot88=1064>0\).
Horizontal strict concavity and the zero derivative at \(t(y)\)
give \(M_1(y)\ge\Re Q(1/4+ih_*;y)\), proving the claim.
\(\square\)

## 5. Every part of the original finite sum

Use the factor-free bounds proved in
[the end-range theorem, equations (4), (5), (9a), (10), (12a)](research_mixed_next_selected_first_wall_rows.md).
They bound the literal conditional rows before multiplication
by any cap. At \(a=1/2\), put
\[
 F(t)=L(t)+J(\tfrac12+t)-J(\tfrac12)-3J(t),\qquad
                          L(t)=-2J((1-t)/2).
                                                               \tag{25}
\]
Uniform zero-safe finite-product estimates give each whole-disk
row rate \(F(j/N)+\tau\), with a polynomial prefactor, for
every fixed tolerance \(\tau>0\). The cited proofs give
\[
 \begin{array}{ll}
 F(t)<7/15+1/100,& t\ge1/2-2\varepsilon,\\
 F(t)<77/160+1/100,&0\le t\le1/16+\varepsilon_- ,
 \end{array}                                                    \tag{26}
\]
for fixed sufficiently small positive collars. Their sizes may
be decreased. Choose \(\varepsilon<1/64\) also smaller than
one quarter of the uniform distance of \(\Re t(y)\) from \(1/2\).
Choose \(\varepsilon_-\) small enough that
\(1/16+\varepsilon_-<1/8\).
Use the original half-grid cuts
\[
 \begin{gathered}
 L_N=\lfloor N/16\rfloor+1,\qquad
 K_N=\lceil N(1/2-\varepsilon)\rceil,\\
 \ell_N=(L_N-1/2)/N,\qquad u_N=(K_N-1/2)/N .
 \end{gathered}                                                  \tag{27}
\]
They have fixed positive real distance from \(t(y)\), for all
large \(N\), and lie inside \([1/20,1/2)\).

A physical row has degree \(j\) in \(Y\). Its disk bound at
radius \(R\ge1\) therefore costs at most \((j/N)\log R\).
The same bound for the continuous real phase follows directly
from the centered-arc argument in the end-range theorem,
equation (21), whenever the cut is below \(1/2\).
Thus the upper physical end and the upper real cut have rate
at most
\[
 E_+=\frac7{15}+\frac1{100}+\frac{\pi}{50}
                   <\frac{13}{24}-\frac3{1400}.
                                                               \tag{28}
\]
The lower physical end and lower real cut have rate at most
\[
 E_-=\frac{77}{160}+\frac1{100}+\frac{\pi}{400}<\frac12.
                                                               \tag{29}
\]
For the last inequalities use \(\pi<22/7\).
Equations (28)--(29) pay the complete omitted physical sums,
including \(j=0,N-1\), without dividing by a numerator product.

For the retained rows the canonical interpolation is exactly
\[
 T_N(t;y)=e^{\pi iNt}\Pi_N(\tfrac12+t)\Pi_N(y+t)
                         E_N(\tfrac12)E_N(y)E_N(t)^3.
                                                               \tag{30}
\]
At \(t=j/N\) it equals the summand of (1). All factors remain
in their original regular strips on
\[
               \ell_N\le\Re t\le u_N,\qquad |\Im t|\le2.
                                                               \tag{31}
\]
The exact residue identity from
[the alias theorem, equation (14)](research_mixed_next_far_half_conditional_aliases.md)
is
\[
 \begin{split}
 \sum_{j=L_N}^{K_N-1}T_N(j/N;y)
   &=N\int_{\ell_N}^{u_N}T_N(t;y)\,dt+\mathcal A_N(y),\\
 \mathcal A_N
   &=\frac{N}{2i}\left\{
       \int_{\partial\mathcal R^+}T_N(t)[\cot(\pi Nt)+i]\,dt+
       \int_{\partial\mathcal R^-}T_N(t)[\cot(\pi Nt)-i]\,dt
                         \right\}.
 \end{split}                                                    \tag{32}
\]
The outer boundary is positively oriented.
Each \(\partial\mathcal R^\pm\) includes the corresponding
halves of both vertical sides; the main real segment is not
part of either. The constant residue mode has density \(+N\).

The proof of the cited alias theorem applies uniformly for
\(0\le H\le1/100\), not just its stated upper endpoint:
its only upper-height input is
\(e^{2\pi(h+H)}\le e^{\pi/50}\) when \(h\le0\).
Its other original argument inequalities hold at every height.
In particular throughout (31),
\[
 \Re Q(v+ih;y)-\Re Q(v;y)\le
 \begin{cases}
   (9\pi/5)h,&h\ge0,\\
   (15\pi/8)|h|,&h\le0.
 \end{cases}                                                    \tag{33}
\]
On the two half-grid sides the alias kernels have modulus at
most \(2e^{-2\pi N|h|}\). Thus their integrands have, relative
to the real cut, additional rates at most \(-\pi h/5\) above
and \(-\pi|h|/8\) below. Equations (28)--(29) pay these
**entire** vertical alias currents, up to height two.
No curvature assertion outside \(|h|\le3/25\) is needed.

For the horizontal aliases, the independent factor-free
estimate in that theorem, equation (17), is
\[
 F(v)<6/5\qquad(\ell_N\le v\le u_N).
                                                               \tag{34}
\]
Its proof uses only \(L(v)\le v\log2\),
\(J(1/2+v)-J(1/2)\le v\log2\), and \(-J(v)<1/6\).
The radius costs at most \(\pi/100\) on this interval.
At heights \(\pm2\), (33) and the kernels give an alias
loss at least \(\pi/4\). Hence their conditional rate is
\[
 \frac65+\frac{\pi}{100}-\frac\pi4
      =\frac65-\frac{6\pi}{25}<\frac{12}{25}<\frac{13}{24}.
                                                               \tag{35}
\]
This is a bound on \(T_N\) with its exact contour density,
before any multiplication by \(U_0\).

It remains to move the main integral in (32). Move its real
segment to height \(h_*=\Im t(y)\), retaining the two vertical
connecting segments at \(\ell_N,u_N\). At their real ends
(28)--(29) apply. At their translated ends, Lemma 2 and
the zero derivative at \(t(y)\) give
\[
 \Re Q(v+ih_*;y)
 \le M_1(y)-\frac{3\pi}{50}(v-\Re t(y))^2,
                                      \qquad v=\ell_N,u_N.
                                                               \tag{36}
\]
The squared distances have a fixed positive uniform lower
bound. Vertical convexity on the interval between \(0\) and
\(h_*\) bounds each entire unweighted connector by the larger
of its endpoint rates. They too are strictly below \(M_1(y)\).

Uniform regular-strip factorial estimates on (31), the
zero-safe physical-product estimates, and compactness now
supply constants \(\eta>0,C,B\), independent of parity, such
that the sum of all the just-listed errors is bounded by
\[
                         CN^B e^{N(M_1(y)-\eta)}.
                                                               \tag{37}
\]
Tolerances are chosen inside the strict reserves only after
the collars and critical-point distances have been fixed.

## 6. The complete packet and its scope

Use the original nonzero factorial symbol
\[
 a_0(z)=\sqrt{2\sin\pi z}\,e^{-i\pi z/2},\qquad
 b(t;y)=\frac{a_0(t+1/2)a_0(t+y)}
                      {a_0(t)^3a_0(1/2)a_0(y)} .
                                                               \tag{38}
\]
The branches continue from the positive real sine chamber.
This is precisely the \(\beta=1\) row symbol in
[the original local source, equation (16)](research_mixed_three_four_next_local_source.md).
The original factorial expansion gives
\[
 T_N(t;y)=N^{-3/2}b(t;y)e^{NQ(t;y)}
                               (1+O_{\mathrm{hol}}(N^{-1}))
                                                               \tag{39}
\]
on a fixed neighborhood of the translated main paths.
No \(\kappa_N\) factor is present in this conditional source.

**Theorem 4.** There is a fixed open neighborhood \(\mathcal V\)
of \(\mathcal Y\) on which the complete original polynomial
satisfies
\[
 \boxed{\quad
 C_{1,N}(-1,e^{-2\pi iy})
   =N^{-1}\,\mathcal B(y)e^{N\Theta(y)}
                      (1+O_{\mathrm{hol}}(N^{-1})),\qquad
 \mathcal B(y)=
       \frac{\sqrt{2\pi}\,b(t(y);y)}
                    {\sqrt{-Q_{tt}(t(y);y)}}\ne0 .
 \quad}                                                        \tag{40}
\]
The square root has positive real part at the base strip,
where \(\Re(-Q_{tt})>0\), and is then continued holomorphically.
The error and all fixed \(y\)-derivatives of the normalized
relative error are \(O(N^{-1})\) on smaller neighborhoods.
The theorem holds along both even and odd levels.

*Proof.* Horizontal strict concavity gives a unique,
nondegenerate maximum at \(t(y)\); (39) and the oriented
horizontal Gaussian give the coefficient in (40).
The three powers are row \(N^{-3/2}\), density \(N\),
and Gaussian width \(N^{-1/2}\), giving \(N^{-1}\).
All other pieces of the exact finite source have the
exponential gap (37).

For the holomorphic assertion, fix a small neighborhood of
each base \(y_0\in\mathcal Y\). Keep its cuts and auxiliary
contours fixed. The physical end bounds persist by uniform
continuity of their zero-safe product rates; the bounded
contour gaps persist by continuity of the original phases.
Move only a small central portion of the main path through
the continued critical point, retaining the short connectors
in its already paid outer portion. Compactness gives one
fixed neighborhood of the whole parameter set. The local
roots and symbols agree on overlaps by Lemma 1. Cauchy's
formula gives the stated normalized derivatives.
\(\square\)

For even \(N\), the identity
\[
 p_j(-1)=\frac{(r^2;r^2)_j}{P_j}
                                                               \tag{41}
\]
makes the rows with \(j\ge N/2\) vanish. For odd \(N\) those
rows generally do not vanish; (28) pays all of them.
Neither case was used to infer an off-grid cancellation.

The full half-cap saddle from
[the separate cap theorem](research_mixed_half_face_cap_critical_point.md)
can now be paired with the genuine conditional action
\(\Theta(y)\) in a local joint calculation. Equation (40)
does not bound the complete cap by its central integral,
pay its private real cuts, or prove that the resulting
product lies below the reference-dependent affine action of
the selected ordinary-next \((0,1,\beta)\) source.
Those statements require their own comparison or grouped
contour argument. No terminal-four action or new knot-family
conclusion is imported here.
