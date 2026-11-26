# The initial incoming interval and taper at the actual cap-343 heights

Private research proof, 8 November 2026. The initial real interval
and its left taper satisfy the required exponential bound for the
actual words beginning \(343\), of length at least five. The proof
uses two new inputs: the complete central profile comparisons and
the complete type-three attachment for a bounded preceding factor.
The first incoming transport itself is unchanged.

This note does not invoke the older theorem whose hypothesis was
\(R\le7/10\). In particular its scalar reduction of all upper next
rates to two endpoints is not used.

## 1. The actual family, paths and finite density

Use the original complete word in powers three and four beginning
\(343\), of length \(m\ge5\). Keep its critical reference and the
notation of
[the actual central theorem](research_mixed_next_three_actual_central_completion.md):
\[
(a_*,s_*,y_*,t_*,z_*)=(t_1,s_2,t_2,s_3,t_3),\qquad
h_a=\Im a_*,\quad h_s=\Im s_*,\quad h_y=\Im y_*,
\quad h_t=\Im t_*,\quad h_z=\Im z_* .
\tag{1}
\]
In particular
\[
\begin{gathered}
-.072<h_a<0,\qquad -.102<h_s,h_y<-.001,\\
-\frac3{100}<h_t,h_z<\frac1{50},\qquad
\frac7{10}<R=e^{2\pi h_y}<\frac{41}{50},\qquad
e^{2\pi h_s}>\frac45R .
\end{gathered}
\tag{2}
\]
All these heights belong to the actual same reference.
Let
\[
y=q+ih_y,\quad 0\le q\le11/50,\qquad
z=u+ih_z,\quad u\in P=[11/50,9/20],\qquad
Y=e^{-2\pi iy},\quad Z=e^{-2\pi iz}.
\tag{3}
\]
The incoming paths, with their original orientations, are
\[
\begin{split}
\Gamma_{\mathrm{in}}&=[0,1/10],\\
\Gamma_{\mathrm{tap}}
&=\{a(x)=x-i\lambda(x-1/10):1/10\le x\le11/50\},\\
\lambda&=-h_a/(3/25)\in(0,3/5).
\end{split}
\tag{4}
\]
The taper ends at \(a_0=11/50+ih_a\).

For \(r=e^{-2\pi i/N}\), define
\[
P_j=(r;r)_j,\qquad p_j(V)=(rV;r)_j,\qquad X=e^{-2\pi ia},
\qquad
C_{\beta,N}(V,W)=
\sum_{j=0}^{N-1}\frac{V^{-j}p_j(V)p_j(W)}{P_j^{2+\beta}} .
\tag{5}
\]
Let \(U_{0,N}(w,X)\) be the complete original cap, defined in
equation (6) of the actual central theorem, and let \(d_N\) be the
original degree-at-most-\((N-1)\) polynomial satisfying
\(d_N(r^b)=P_b^{-1}\). The density is
\[
\mathcal D_N(a;y,z)=
U_{0,N}(w,X)C_{1,N}(X,Y)d_N(Y)C_{0,N}(Y,Z).
\tag{6}
\]
There is no outgoing halfweight for the next type three.
The affine action bound \(\Lambda_{123}(z)\) is unchanged.
At the actual output it satisfies
\(\Lambda_{123}(z_*)=\Re\mathcal P_0^+(-2,z_*)\), with the
original holomorphic action and its original constant.

**Theorem.** For all real ordinary colors \(w\in[-2,2]\), both
level parities, and all sufficiently large \(N\),
\[
|\mathcal D_N(a;y,z)|
\le C N^B e^{N\{\Lambda_{123}(z)-10^{-12}\}},
\qquad a\in\Gamma_{\mathrm{in}}\cup\Gamma_{\mathrm{tap}} .
\tag{7}
\]
Either oriented integral has the same exponential bound with its
original measure \(+N\,da\). At fixed base references, their
normalizations by \(e^{-N\mathcal P_0^+(w,z)}\) have every fixed
mixed derivative bounded on sufficiently small fixed neighborhoods
with deficit \(10^{-13}\).

## 2. The two inputs concerning the following kernel

Use the original primitive \(g\) and literal phases
\[
Q_\beta(v;b,c)=g(b+v)+g(c+v)-(2+\beta)g(v)
                         -g(b)-g(c)+2\pi ibv .
\tag{8}
\]
Write \(E_0(t;y,z)=\Re Q_0(t;y,z)\) for real \(t\), with its
continuous integral value at endpoints, and
\[
L_0=E_0(1;y,z)=-\log R+2\pi(h_z)_+ .
\]
For fixed \(y,z\), define the compact set of next rates
\[
\begin{split}
\mathscr P(y,z)={}&
\{\Re Q_0(t_R+ih_t;y,z):3/20\le t_R\le1/2\}\\
&{}\cup\{E_0(3/20;y,z),E_0(1/2;y,z)\}\\
&{}\cup\{E_0(t;y,z):1/2\le t\le1\}.
\end{split}
\tag{9}
\]
The last group includes \(L_0\). It retains every upper physical
rate; it is not replaced by the old two-endpoint envelope.

The original low-row and complete-current estimates, with the
uniform positive upper-row estimates, give for every \(\tau>0\)
\[
|d_N(Y)C_{0,N}(Y,Z)|
\le C_\tau N^{B_\tau}
 \exp N\{\max_{\varphi\in\mathscr P(y,z)}\varphi-\Re g(y)+\tau\}.
\tag{10}
\]
The lower main height \(h_t\) may have either sign. The current
estimates retain both horizontal terms, four weighted vertical
pieces and two unweighted joins. The upper-row estimates retain
numerator zeros and the true last index.

The first required input is a profile comparison at \(a=a_0\):
\[
B_U(11/50)+\Re Q_1(s;a_0,y)+\varphi-\Re g(y)
<\Lambda_{123}(z)-10^{-10},
\qquad \varphi\in\mathscr P(y,z),
\tag{11}
\]
for the first main \(s=s_R+ih_s\), \(1/8\le s_R\le1/2\),
and the two real cuts \(s=1/8,1/2\).
Here \(B_U\) is the original complete-cap supporting plane.
Each retained cap main, cut and end profile at \(a_0\) is bounded
by this same plane before any first-index summation.

Equation (11) follows from the profile proofs underlying the
actual central theorem, rather than from the modulus of its final
signed sum. The next main and lower cuts use the
[complete-first below-half proof](research_mixed_next_own_three_below_half_complete_first.md).
For all upper real rates the original band comparisons, the
[small-index logarithmic inequality](research_mixed_next_three_small_reflected_logarithmic_bound.md),
the [intermediate-strip comparison](research_mixed_next_own_three_shallow_upper_strip_reduction.md),
and [correlated last transport](research_mixed_next_three_correlated_last_row_transport.md)
give (11) with the first profile still attached.
The first main is clipped only by its original same-coordinate
index inequalities; those extend the bound to the stated full
main range. The intermediate-strip proof may move \(q,t\) while
proving its endpoint bound, but its conclusion is an inequality
for each original \(q,t\). Those values remain fixed during the
incoming transport below. No next positive-height main is moved
by a negative-height transport formula.

The second input is
[the actual bounded-prefix theorem](research_mixed_next_three_actual_bounded_prefix.md).
Put \(B_0=2383/1500\). If a preceding factor satisfies, for every
\(\tau>0\),
\[
|V_N|\le C_\tau N^{B_\tau}e^{N(B_0+\tau)},
\tag{12}
\]
uniformly on its stated domain, then
\[
|V_Nd_N(Y)C_{0,N}(Y,Z)|
\le C N^B e^{N\{\Lambda_{123}(z)-1/200\}} .
\tag{13}
\]
This is a bound for the complete following kernel and weight.
A complete cap times a positive first-row group is an admissible
\(V_N\) when its own bound (12) has been established.

## 3. Incoming transport of the first profiles

We use the first-source inequalities of
[the original initial/taper proof, Sections 2--3](research_mixed_next_lower_left_incoming_initial_taper.md).
Their formulas involve the first cap, \(C_{1,N}\), and \(y\);
they do not involve \(z\), \(h_t\), or a following own-type flag.
Their radius hypotheses are \(1/2<R<1\), or \(0<R\le1\).
Thus (2) satisfies them. The next-type-four theorem in that note
is not being imported; only its explicitly stated first-source
inequalities are used.

Here is their full controlling inventory. On the taper the real cut is
\[
\ell(x)=7/100+x/4,\qquad
\ell(1/10)=19/200,\quad \ell(11/50)=1/8 .
\tag{14}
\]
For the original cap profile \(\Psi_0(e,a)\), the fixed-real-index
incoming derivative of \(\Psi_0+Q_1\) is
\[
H=\Re D_a+\lambda\Im D_a,\qquad
D_a=g'(e+a)+g'(a+v)-2g'(a)+2\pi iv .
\tag{15}
\]
It is independent of \(y,z\) and the next private index.
The cap envelope has
\(e=u_e+ik\), \(27/100\le u_e\le49/100\),
\(-19/1000\le k\le37/1000\), together with its separated true
endpoint profile. The source supplies the following exact bounds:
\[
\begin{array}{c|c|c}
x\text{ interval}&H>&\exp(\Re Q_{1,s}(\ell(x)))>\\ \hline
[1/10,9/50]&-118/875&9/5\\
[9/50,11/50]&-139/800&135/64 .
\end{array}
\tag{16}
\]
Because \(\ell'=1/4\), both give
\[
\frac d{dx}\Re\{\Psi_0(e,a(x))+Q_1(\ell(x);a(x),y)\}
>1/200 .
\tag{17}
\]
The true endpoint profile has the same positive transport, as
verified separately in the cited source.

Every first low physical row increases to this cut. Indeed its force is
\[
\exp(\Re Q_{1,s}(v;a,y))
=\frac{|T-e^{-2\pi i(x+v)}|\,|1-Re^{-2\pi i(q+v)}|}
       {(2\sin\pi v)^3},\qquad T=e^{-2\pi\Im a}\ge1 ,
\tag{18}
\]
and \(x+2v<1,\ q+2v<1/2\) give the strict lower bound
\(\cos(\pi v)/(2\sin\pi v)>1\) for \(0<v\le\ell(x)\).
The zero row is retained with its exact value one.

At the original negative first height \(h_s\), the added segment
\(\ell(x)\le s_R\le3/20\) increases to \(3/20+ih_s\).
This is the source's equations (16)--(17), which require only the
nonpositive first heights and \(R<1\). For the rest of the main
segment, and for the real half cut, the original incoming derivative
transports to \(a_0\). At that endpoint (11) applies to every
\(\varphi\) in (9).

For completeness, the current estimates on
\(19/200\le s_R\le1/2\) retain the exact inequalities
\[
\begin{split}
-203\pi/200<\Im Q_{1,s}<103\pi/100
       &\qquad(\Im s\le0),\\
\Im Q_{1,s}>-19\pi/10&\qquad(\Im s\ge0).
\end{split}
\tag{19}
\]
They give losses \(97\pi/500\) and \(29647\pi/100000\) for the
horizontal aliases at heights \(-1/5\) and \(4\), relative to the
same first main. All four weighted sides decrease away from their
real cuts. Both unweighted joins between \(h_s\) and zero are
convex; on the added low-index strip the curvature witness is
\(9\pi/22\), and the remaining strip uses the original cotangent
comparison. Thus every first current is bounded by a main or
real-cut endpoint already covered by (11), (17).

Throughout these comparisons the next rate \(\varphi\) and
\(-\Re g(y)\) are constant in \(x\) and the first private index.
They remain attached without changing any derivative or alias loss.
Combining these source bounds with (10) is therefore legitimate
before either complete kernel is summed.

## 4. First upper rows and the incoming seam

Let \(E_1\) be the original first physical row rate and
\(\delta_a=-2\pi\Im a\). With reflected index \(v=1-j/N\),
Section 4 of the original initial/taper source proves
\[
\begin{array}{c|c}
\text{range}&E_1(1-v;a,y)\text{ is at most}\\ \hline
9/50\le v\le1/2&E_1(1/2;a,y)\\
0\le v\le9/50,\ x\ge9/50&\delta_a\\
0\le v\le9/50,\ x\le9/50&\delta_a+11/100 .
\end{array}
\tag{20}
\]
These are first-kernel statements valid for \(0<R\le1\).
Their reflection retains the incoming chirp:
\[
\begin{split}
E_1(1-v)-\delta_a
=3J(v)&-\int_0^v\log|T-e^{-2\pi i(x-s)}|\,ds\\
      &-\int_0^v\log|1-Re^{-2\pi i(q-s)}|\,ds .
\end{split}
\tag{21}
\]
The half alternative is paid by the profile transport above.
The complete-cap bound and the taper correlation give the
strict preceding-factor ceilings
\[
11099/7000<B_0,\qquad 10813/7000<B_0
\tag{22}
\]
for the other two positive groups, respectively.
Apply (13) to each complete cap times its positive row group.
This uses a bound for that whole group; it does not extract
individual cap coefficients from a coherent cap bound.

Near \(X=1\), the original finite seam estimate is uniform on
\(|Y|\le1\). Its rate tends to
\[
101/125+7/15=478/375<B_0 .
\tag{23}
\]
More explicitly its error in the rate is
\(2\Omega(\epsilon)-\log(1-\epsilon)+\tau\), where
\(\Omega(\epsilon)=\log(1+\epsilon/2)
+(\epsilon/2)\log(1+2/\epsilon)\), on \(|X-1|\le\epsilon\).
Choose a fixed small neighborhood and tolerances inside (23);
then (13) bounds the full density there.

On the remainder of the initial real interval, keep the full
cap envelope, including its extra real profile
\(49/100\le e\le1/2\), with fixed first cuts \(19/200,1/2\).
At every first-current point the source's exact derivative is
\[
\frac d{dx}\Re\{\Psi_0(e,x)+Q_1(v+i\sigma;x,y)\}
=\log\frac{|1-e^{-2\pi i(e+x)}|
             |e^{-2\pi\sigma}-e^{-2\pi i(x+v)}|}
               {(2\sin\pi x)^2}
>\log(11/8)>0 .
\tag{24}
\]
It transports each profile to \(x=1/10\), already bounded by
the taper argument. The extra real cap profile clips to \(e=49/100\)
there, within the original proved cap envelope.
The separated true cap endpoints have preceding-factor rate
\[
3/5+23/100+7/15=389/300<B_0,
\tag{25}
\]
so (13) covers them independently. All low and upper first
physical rows use (18), (20), including their true endpoints.

## 5. Finite assembly and local derivatives

The first row ranges are exactly
\[
0\le j<L_N,\qquad L_N\le j<M_N,\qquad M_N\le j<N,
\]
where \(M_N=\lceil N/2\rceil\) and
\(L_N=\lfloor N\ell(x)\rfloor+1\); on the initial interval
\(\ell=19/200\). Their half-grid cuts are
\((L_N-1/2)/N\) and \((M_N-1/2)/N\).
The original canonical interpolant is
\[
e^{2\pi iNas}
\frac{\Pi_N(a+s)\Pi_N(y+s)}
     {\Pi_N(a)\Pi_N(y)\Pi_N(s)^3}.
\tag{26}
\]
Its exact cotangent decomposition retains the main measure
\(+N\,ds\), both horizontal terms, four weighted vertical
pieces and both unweighted joins. The source inequalities above
apply to all those pieces. A sufficiently small fixed enlargement
of the cut intervals absorbs their \(O(N^{-1})\) displacements.
Either adjacent partition is bounded at a moving-cut jump.

The next factor is bounded by the complete rate family (9);
its own low, middle and upper rows and all canonical currents
are retained in (10). At \(q=0\), the canonical reciprocal
factorial uses the original inward-seam continuation. The
different finite polynomial \(d_N\) uses its forced upper
envelope with rate \(-\Re g(y)\). Neither replaces the other.

The paired profiles retain deficit \(10^{-10}\); the separate
preceding-factor groups have the larger deficit \(1/200\).
Choose the sum of all finite tolerances inside these reserves.
Polynomially many rows, canonical measures and bounded path
lengths change only powers of \(N\). This gives the conservative
common gap \(10^{-12}\) in (7). The incoming measures are
\(+N\,dx\) and \(+N(1-i\lambda)\,dx\), respectively.

For fixed \(a,y\), the complete density is polynomial of degree
at most \(N-1\) in \(w\) and in \(Z\); the fixed-path integrals
have the same degree bounds. The existing real-color and
logarithmic-arc continuation therefore costs an arbitrarily small
fixed exponential rate. Together with the equality of the action
at the actual output and Cauchy's formula on smaller neighborhoods,
this proves the normalized derivative assertion.
The reference heights, base paths and any intermediate cuts are
fixed before differentiation.

This proves the two incoming pieces on the actual geometric
family. The right incoming path, filter correction and remaining
signed shared-variable contours require their respective separate
arguments. No noncancellation conclusion for the complete
invariant follows from this theorem alone.

