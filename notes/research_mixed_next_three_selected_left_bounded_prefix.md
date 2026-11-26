# Attaching a bounded preceding factor on the selected left interval

Private research proof candidate, 8 November 2026. The complete
next type-three kernel can be attached to a preceding factor of
rate at most \(2383/1500\), on the upper shared contour to the
left of the central interval. This uses the actual outgoing
coordinate of words beginning \(343\), rather than an independently
varied outgoing point in the old larger interval.

The statement includes the forced Fourier polynomial, all next
indices and every contour term. It does not assert that an
uncontrolled preceding factor has the required bound. No
mathematical numerical evaluation or frozen-source edit is used.
Adoption requires complete source and proof reviews.

## 1. Actual references and statement

Use the original references of complete words in powers three and
four beginning \(343\), of length at least five. Keep their actual
heights \(c=\Im t_2^*\), \(h_t=\Im s_3^*\), \(h_z=\Im t_3^*\),
original logarithmic lifts, and affine action \(\Lambda_{123}(z)\).
The [actual bounded-prefix theorem](research_mixed_next_three_actual_bounded_prefix.md)
and [open-word inheritance](research_mixed_open_word_window_inheritance.md)
give
\[
 7/10<e^{2\pi c}<41/50,\qquad
 -3/100<h_t,h_z<1/50,\qquad
 3/10<\Re t_3^*<39/100.
 \tag{1}
\]
In this note
\[
 y=q+iH,\quad H=1/100,\quad 0\le q\le q_0=11/50,
 \qquad z=u+ih_z,\quad 3/10\le u\le39/100.
 \tag{2}
\]
All reference data are fixed while these real integration or target
coordinates vary. The hypotheses are the original correlated
ones; (1) is not a new independent box of critical points.

Set
\[
 R=e^{2\pi H},\quad U=e^{2\pi h_t},\quad
 A=U^{-1},\quad \rho=e^{2\pi h_z},\qquad B_0=2383/1500.
\]
The bounds already proved in
[selected left profiles](research_mixed_next_three_selected_left_main_profiles.md)
include
\[
 53/50<R<16/15,\quad 4/5<U,\rho<8/7,\quad A>7/8 .
 \tag{3}
\]
For \(D=N-1\), \(r=e^{-2\pi i/N}\), put
\[
 P_j=(r;r)_j,\quad p_j(V)=(rV;r)_j,\qquad
 C_{0,N}(Y,Z)=\sum_{j=0}^{D}
                 \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2},
 \quad Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
 \tag{4}
\]
The polynomial \(d_N\) has degree at most \(D\) and retains its
original values \(d_N(r^b)=P_b^{-1}\).

**Theorem.** Suppose, on this domain and for every \(\tau>0\),
\[
 |V_N|\le C_\tau N^{a_\tau}e^{N(B_0+\tau)}.
 \tag{5}
\]
Then the complete original next factor satisfies, at both parities,
\[
 \left|V_Nd_N(Y)Y^{-N}C_{0,N}(Y,Z)\right|
       \le C N^a e^{N\{\Lambda_{123}(z)-1/400\}} .
 \tag{6}
\]
The preceding factor is independent of the next private summation
index. No holomorphy of \(V_N\) is required for this pointwise
statement, and no derivative conclusion is inferred from (5).

## 2. Calibration at the old endpoint

Keep the bare phase
\[
 Q(t;y,z)=g(y+t)+g(z+t)-2g(t)-g(y)-g(z)+2\pi iyt,
 \qquad g'(w)=\operatorname{Log}(1-e^{-2\pi iw}),
 \tag{7}
\]
with the original constant in \(g\). At the selected height its
two weight rates are
\[
 W_{\rm fac}(y)=-\Re g(y)-2\pi H,\qquad W_{\rm force}(y)=0.
 \tag{8}
\]
Section 2 of the actual bounded-prefix theorem gives, at
\(y_c=q_0+ic\),
\[
 \begin{split}
 B_0+\Re Q(t;y_c,z)-\Re g(y_c)&<\Lambda_{123}(z)-1/50,\\
 B_0+L_c-\Re g(y_c)&<\Lambda_{123}(z)-1/50,
 \qquad L_c=-2\pi c+\log_+\rho .
 \end{split}                                                    \tag{9}
\]
The first line covers all original main indices
\(t=v+ih_t,\ 3/20\le v\le1/2\), and the two real cuts
\(t=3/20,1/2\). These are individual phase bounds, with the
original marginal allocation, before any signed sum.

We first move (9) vertically, still at \(q=q_0\). Write
\[
 \mathcal A(v,k)=\arg(1-e^{2\pi k-2\pi iv}),\quad
 G(k)=\Re g(q_0+ik),\quad \Phi(k)=\Re Q(t;q_0+ik,z).
 \tag{10}
\]
For \(0<v<1\), the argument lies between zero and
\(\pi(1-2v)\); for \(k\le0\) it lies between zero and
\(\pi(1/2-v)\). Consequently
\[
 \Phi'=\mathcal A(q_0,k)-\mathcal A(q_0+\Re t,k+\Im t)
                       -2\pi\Re t,\qquad G'=-\mathcal A(q_0,k).
 \tag{11}
\]
For \(c\le k\le0\), splitting at \(q_0+\Re t=1/2\) gives
\[
 (\Phi-G)'\le
 \begin{cases}
 \pi(1-2q_0-2\Re t),&q_0+\Re t\le1/2,\\
 0,&q_0+\Re t\ge1/2.
 \end{cases}                                                    \tag{12}
\]
For \(0\le k\le H\), the same split gives
\[
 (\Phi-G-2\pi k)'\le
 \begin{cases}
 -2\pi(2q_0+\Re t),&q_0+\Re t\le1/2,\\
 -\pi(1+2q_0),&q_0+\Re t\ge1/2.
 \end{cases}                                                    \tag{13}
\]
Also \(-c<3/(16\pi)\): indeed \(e^{3/8}>185/128>10/7\)
and (1) implies \(-2\pi c<\log(10/7)<3/8\).

For main indices with \(\Re t\ge1/6\), (12)--(13) bound
the increase from the unselected rate in (9) to the factorial
selected rate by
\[
             17/400-91/2500=61/10000.
 \tag{14}
\]
For the real low cut, the corresponding bound is
\[
             39/800-177/5000.
 \tag{15}
\]
For the real half cut it is nonpositive. In obtaining the
negative terms in (14)--(15), only \(\pi>3\) was used.
Thus the selected factorial low-cut reserve is greater than
\[
           1/50-39/800+177/5000=133/20000.
 \tag{16}
\]
The main reserve is greater than \(139/10000>1/100\).

For the forcing branch, (11) gives \(\Phi'\le0\) below
height zero for every \(\Re t\ge3/20\). Above zero its
upper bound is \(13\pi/50\); at the real half cut it is
nonpositive. Furthermore \(G(c)<0\). For example this sign
follows directly by integrating the argument of
\(1-se^{-2\pi iq_0}\) over \(0<s<e^{2\pi c}<1\) in the
dilogarithm formula. Hence
\[
 \Phi(H)-\{\Phi(c)-G(c)\}<13\pi/5000<1/100.
 \tag{17}
\]
The forcing main and low-cut reserves exceed \(1/100\);
the half-cut reserve remains \(1/50\).

## 3. Transport along the selected interval

The lower clipping of the next main index to \(v=1/6\)
is proved in Section 2 of the selected-left profile theorem.
There is a stronger upper clipping here, using (2):
every main with \(2/5\le v\le1/2\) decreases as \(v\)
increases. Its squared force is bounded above by
\[
 \frac{(1+U)^2(1+64U^2/49+16U/21)}
             {(1+U^2+8U/5)^2}<1 .
 \tag{18}
\]
Indeed \(\cos2\pi v<-4/5\), whereas
\(\cos2\pi(u+v)>-1/3\), because \(u+v\in[.7,.89]\).
The denominator minus numerator in (18), divided by \(U\), is
\[
 \frac{46}{105}+\frac{2683}{3675}U
          -\frac{128}{735}U^2-\frac{15}{49}U^3>\frac{29}{150}>0.
 \tag{19}
\]
For the displayed lower bound use \(U>4/5,\ U^2<4/3,\
U^3<3/2\), and bound the four coefficients respectively by
\(2/5,7/10,1/5,1/3\). Thus it suffices to consider
\[
                          1/6\le v\le2/5 .
 \tag{20}
\]

Put \(D_q=|1-Y|^2\) and
\(U_2=|A-Re^{-2\pi i(q+v)}|^2\). The exact derivatives are
\[
 e^{2\partial_q(\Re Q+W_{\rm fac})}=U_2/D_q^2,\qquad
 e^{2\partial_q(\Re Q+W_{\rm force})}=U_2/D_q .
 \tag{21}
\]
On the first three subintervals
\([0,.1],[.1,.15],[.15,.2]\), Table (18) of the selected-left
profile theorem gives respectively
\[
\begin{array}{c|c|c}
q\text{ interval}&D_q\text{ upper bound}&U_2\text{ lower bound}\\\hline
[0,1/10]&1/2&3/4\\
[1/10,3/20]&1&113/64\\
[3/20,1/5]&3/2&733/320 .
\end{array}                                                     \tag{22}
\]
Each line has \(U_2>\max(D_q,D_q^2)\).

On \([.2,.22]\), the shifted interval in (20) lies in
\([11/30,31/50]\), where \(\cos2\pi(q+v)<-33/50\).
One elementary witness is
\(\cos(4\pi/15)>\cos(21/25)>33/50\).
For the latter use
\[
 \cos x\ge1-x^2/2+x^4/24-x^6/720,\quad x=21/25,
 \quad x^4/24>1/50,\quad x^6/720<1/1000.
 \]
The resulting lower bound is \(3331/5000>33/50\).
It follows from (3) that
\[
 U_2>49/64+2809/2500+12243/10000
      >621/200>31/10>(44/25)^2>D_q^2 .
 \tag{23}
\]
Also \(D_q<44/25<31/10\). Thus both main rates
increase toward \(q_0\), and (14),(17) apply uniformly.

At the real low cut use \(A=1,v=3/20\) in (21).
The first three numerator bounds may be replaced by
\(16/25,2,13/5\). On the last interval the shifted cosine
is below \(-1/2\), so
\[
                  U_2>7959/2500>(44/25)^2.
 \tag{24}
\]
Both rates increase, retaining (16).

The real half cut has the same first three comparisons.
On the last interval \(U_2>5/2,\ D_q^2<25/8\).
The forcing rate increases, while the factorial derivative
exceeds \(-1/8\), since \(\log(5/4)<1/4\).
Transport over length \(1/50\) costs less than \(1/400\).
Its uniform reserve therefore exceeds \(7/400\).

The last-index profile is \(L_H=\log_+\rho\).
For completeness its uniform selected bound follows without
transport in \(q\). The old sine-integral bound
\(-J(1/6)<13/80\), used in the
[high-right insertion estimate](research_mixed_next_right_insertion_actual_high_band.md),
and the harmonic maximum principle give
\(-\Re g(q+i\log T/(2\pi))\le13/80\) for \(T=R^{-1}<1\).
The dilogarithm inversion formula with the original upper-side
lift yields
\[
 W_{\rm fac}(q+iH)
 =-\Re g(q+i\log T/(2\pi))-\pi H(1+2q)\le13/80 .
 \tag{25}
\]
At the calibration point \(G(c)<0\) and
\(-2\pi c>\log(50/41)>18/91>13/80\). Consequently both
\(B_0+L_H+W_\nu\) are strictly smaller than
\(B_0+L_c-G(c)\), which is bounded by (9).

We have proved that every next main, real low, real half,
and last profile, paired with either selected weight and
the constant \(B_0\), has reserve greater than
\[
                              \delta_0=133/20000 .
 \tag{26}
\]

## 4. The positive physical rows

The prefix-independent reduction in
[selected upper physical rows](research_mixed_next_three_selected_left_upper_rows.md)
applies on precisely (2)--(3). In its notation \(F(v)=E(1-v)\),
all rows \(v\le1/5\) satisfy \(F(v)\le L_H-v/400\).
Rows \(v\ge3/10\), and rows \(1/5\le v\le3/10\) with
\(q\ge3/20\), increase to the real half profile.

For \(q<3/20,\ 1/5<v<3/10\), increase \(q,v\) together.
With \(S(v)=2\sin\pi v\) and
\(B(v)=|1-\rho e^{2\pi i(v-u)}|\), the two next-only
multipliers are exactly
\[
 \frac{R S(v)^2}{D_q B(v)},\qquad
 \frac{R S(v)^2}{\sqrt{D_q}B(v)} .
 \tag{27}
\]
Here \(D_q<1,\ S(v)^2>11/8,\ B(v)<9/7\), so both
exceed \(77/72\). Stop at \(q=3/20\) or \(v=3/10\);
the preceding comparison then reaches the real half profile.
Since (26) holds at every stopping coordinate, every upper
physical row has that same reserve. This comparison does not
require a first main profile.

For the lower physical rows \(0<t\le3/20\), the folded
incoming numerator is at least
\(\sqrt{15/16}\,2\sin\pi t\). The outgoing numerator
exceeds \(7/5\): its angle \(u+t\in[.3,.54]\) has cosine
less than \(-3/10\), and \(\rho>4/5\).
Since \(2\sin\pi t<1\), the real force is greater than
\(\sqrt{15/16}(7/5)>1\). Thus the whole low physical
block is bounded by its real low-cut profile, including its
zero row by the endpoint-uniform finite estimates.

## 5. Every term in the middle contour decomposition

For \(3/20\le v\le1/2\), set
\[
 J(v,\sigma)=\Im Q_t(v+i\sigma;y,z)
 =\mathcal A(q+v,H+\sigma)+\mathcal A(u+v,h_z+\sigma)
            -2\mathcal A(v,\sigma)+2\pi q .
 \tag{28}
\]
The elementary argument bounds used in (11), split according
to which of \(q+v,u+v\) exceeds \(1/2\), give
\[
 J\le4\pi/5\quad\hbox{at every height},\qquad
 J\ge-39\pi/50\quad(\sigma\le0),\qquad
 J\ge-113\pi/100\quad(\sigma\ge0).
 \tag{29}
\]
For the upper bound the three cases give, after division by
\(\pi\), \(2-4v-2u,\ 1-2v,\ 2q\).
For the lower bound at negative height they give
\(-1+2v+2q,\ 2q-2u,\ 1-2u-2v\).
At positive height \(H+\sigma>0\); using the positive-height
lower bound on the incoming argument gives
\(-3/2+3v+q,\ -1/2+v+q-2u,\ -2u\).
These prove (29) on the stated domain.

The weighted vertical rates \(\Re Q-2\pi|\sigma|\)
therefore decrease away from zero. At each real cut, both
weighted halves are bounded by the real-cut profile.
Use the original horizontal alias heights \(-1/5\) and \(4\).
Integrating (29) from the original \(h_t\) gives
\[
 \begin{split}
 \Re Q(v-i/5)-2\pi/5
       &\le \Re Q(v+ih_t)-28\pi/125,\\
 \Re Q(v+4i)-8\pi
       &\le \Re Q(v+ih_t)-3\pi .
 \end{split}                                                    \tag{30}
\]
The latter weaker round bound follows already from
\((113/100)(403/100)-8<-3\).

The two unweighted joins are also retained. Write
\[
 C(v,\sigma)=\Re\cot\pi(v+i\sigma),\qquad w=\cot\pi v .
 \]
For \(|\sigma|\le3/100\) and \(v<1/2\), the elementary
cosh bound from the
[complete-current proof, Section 5](research_mixed_next_lower_left_complete_currents.md)
gives \(C(v,\sigma)>(4/5)w\).
The incoming shifted cotangent is at most \(w\). If the
outgoing shifted cotangent is positive, put \(c_u=\cot\pi u<1\);
its value is at most
\[
               \frac{wc_u-1}{w+c_u}<w/2 ,
 \]
because \(w^2-c_uw+2>0\). If it is nonpositive it needs
no upper cost. Thus
\[
 2C(v,\sigma)-C(v+q,H+\sigma)-C(v+u,h_z+\sigma)>0 .
 \tag{31}
\]
At \(v=1/2\), the outgoing term gives strictness directly.
This is convexity of \(\Re Q\) in the vertical private
coordinate. Each join is bounded by its two endpoint profiles.

For fixed \(\epsilon>0\), apply the original exact cotangent
decomposition on \(\epsilon\le q\le q_0\), with half-grid cuts
corresponding to \(\lfloor3N/20\rfloor+1\) and
\(\lceil N/2\rceil\). All canonical arguments remain in
regular strips. Equations (29)--(31) bound its two horizontal
aliases, four weighted sides and two unweighted joins.
The constant-mode integral keeps its original coefficient
\(+N\). The physical low and upper blocks are those in
Section 4, with their actual integer endpoints.

The original uniform factorial and zero-safe numerator bounds,
and the full Fourier-weight bound (8), introduce arbitrarily
small rate tolerances. Their finite sum and the factors of
\(N\) cost only a polynomial. In view of (26), these prove
\[
 |d_N(Y)Y^{-N}C_{0,N}(Y,Z)|
 \le C_\epsilon N^{a_\epsilon}
       e^{N\{\Lambda_{123}(z)-B_0-1/200\}}
               \quad(\epsilon\le q\le q_0).
 \tag{32}
\]

## 6. The endpoint and the finite preceding factor

No canonical symbol at the positive-height seam is needed
to extend (32) to \(q=0\). The exact core in (32) has
Laurent support in \([-D-N,D-N]\): the incoming exponents
of \(C_{0,N}\) lie in \([-D,0]\). Its frequencies therefore
have absolute value less than \(2N\).

Use the elementary arc estimate (8) of
[horizontal complex extension](research_mixed_horizontal_complex_extension.md).
Choose a small fixed halfwidth \(\alpha>0\) and an ellipse
parameter close enough to one that its rate loss for frequencies
bounded by \(2N\) is less than \(1/1000\). The inverse ellipse
contains a fixed neighborhood of its real interval, including
both endpoints. Its extension width \(\delta>0\) depends on
\(\alpha\) and that ellipse, but not on the center of the
interval or on \(N\).

Now choose \(0<\epsilon<\delta\) so that
\([\epsilon,\epsilon+2\alpha]\subset[\epsilon,q_0]\).
Apply (32) on this short interval, with its center
\(\epsilon+\alpha\). The same arc estimate extends the bound
to \(q=0\) and covers the added interval \([0,\epsilon]\).
All arcs and continuation parameters are fixed before \(N\)
varies. This proves the asserted extension of the complete
finite Laurent polynomial, including its forcing term, with
the prescribed rate loss.

Choose that loss below \(1/1000\) and then the tolerance
in (5) below \(1/1000\). Equation (32) leaves a rate gap
greater than \(1/200-2/1000=3/1000>1/400\), proving (6).

The theorem can attach an already bounded raw first contribution
or correction polynomial on this selected interval. It does
not bound the remaining first incoming main contributions,
alter the old filter, or establish the complete upper-left
integral. Such applications require their own preceding-factor
estimates at the selected radius \(R>1\).
