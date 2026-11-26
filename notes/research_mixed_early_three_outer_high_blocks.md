# The two ends of the early first 3,3 high-row block

Research deduction, 10 November 2026. The complete first-three cap
can be combined with all high rows before a fixed reflected cut and
with every sufficiently late row of its adjoining own-three factor.
The last-row calibration holds for every actual first-height sign.
A separate estimate pays the entire true-cap-end contribution when
that height is nonpositive.

The remaining interior wrapped rows are stated explicitly. Neither
an endpoint-only ordinary estimate nor a sign for their descending
quartic crossings is assumed.

## 1. Original reference and finite source

Fix an actual positive three/four open word of length at least three
beginning \(3,3\). Keep the same actual reference and allocation as
the joint low-/half-row and central-source theorems:
\[
 a_*=a_0+ic,\quad b_*=b_0+id,\qquad
 a=x+ic,\quad b=z+id,\quad
 .1\le x\le.22,\quad .22\le z\le.45 .
\tag{1}
\]
The original endpoint and ordinary-image bounds imply
\[
 -.072<c<.021,\quad -.065<d<.068,\qquad
 3/5<r=e^{2\pi c}<23/20,\quad
 13/20<t=e^{2\pi d}<31/20.
\tag{2}
\]
These are the written radius consequences in the
[unwrapped stationary-row theorem](research_mixed_unwrapped_stationary_high_row_transport.md).
No independently chosen containing-box point replaces the reference.

For \(r_N=e^{-2\pi i/N}\), retain the exact rows
\[
 R_{j,N}(a,b)=X^{-j}
  \frac{(r_NX;r_N)_j(r_NY;r_N)_j}{(r_N;r_N)_j^2},
 \quad X=e^{-2\pi ia},\quad Y=e^{-2\pi ib},\quad0\le j<N.
\tag{3}
\]
Let \(U_{0,N}(w,X)\) be the complete first-cap polynomial.
There are no type-four Fourier weights in this first pair.
Its original external scalar and later factors are unchanged.

Write \(E_0(s;a,b)\) for the full unallocated absolute row rate:
\[
 E_0(s)=
 \int_0^s\log|1-e^{-2\pi i(a+u)}|\,du+
 \int_0^s\log|1-e^{-2\pi i(b+u)}|\,du
                   -2J(s)-2\pi cs.
\tag{4}
\]
This includes the first chirp and every revived row through the
wrapped zeros. The original reflection identity gives
\[
 E_0(1)=\lambda,\qquad
                 \lambda=2\pi\{(-c)_++d_+\}.
\tag{5}
\]
The continuous endpoint \(1\) is a rate; it is not an extra finite row.

Retain the original phases \(\Xi_0,F_{00},L_0,\phi_{00}\) and
the plane
\[
\begin{split}
 \Gamma(z)&=\Re L_0(a_*)+\Re\phi_{00}(a_*,b_*)\\
 &+\Re\partial_b\phi_{00}(a_*,b_*)(z-b_0)-\kappa(z-b_0)^2,\\
 \kappa&=1/2500000,\qquad
 \gamma_*=\kappa(a_0-.22)^2>0.
\end{split}
\tag{6}
\]
The first-coordinate marginals cancel exactly. Both first-coordinate
quadratic losses will be retained at the comparison point \(x=.22\).

## 2. The complete cap with the last-row rate

**Lemma 1.** At every actual height in (1), every term of the complete
cap envelope, after adding the last-row rate \(\lambda\), is at most
\[
                         \Gamma(z)-2\gamma_*.
\tag{7}
\]
This includes the physical right-row allowance and the true cap ends.

*Proof.* The complete fixed-height cap theorem retains the main line,
both real cuts, both horizontal aliases and its true endpoints.
For first type three its actual private height is
\(-.019<h_e<.037\).
The lower cap alias has already been compared to this actual main
line in equation (21) of the
[positive-private-height first33 source](research_mixed_early_three_positive_private_central.md):
\[
 \Re\Xi_0(u-.055i,a)-.11\pi
 <\Re\Xi_0(u+ih_e,a)-9\pi/6250.
\tag{8}
\]
That proof uses only the cap variables and the original branch;
it does not require any height sign for the adjoining ordinary index.

Every other cap profile has private radius
\(R=e^{2\pi\Im e}>7/8\), with \(.27\le\Re e\le.49\).
The last-row rate in (5) is independent of \(x\). Its regular joint
derivative is therefore exactly
\[
 \partial_x\{\Re\Xi_0(e,a)+\lambda\}
 =\log(N_e/D),\quad
 N_e=|1-rR e^{-2\pi i(\Re e+x)}|,\quad
 D=|1-r e^{-2\pi ix}|.
\tag{9}
\]
For \(x\le.16\), the original angular bounds give
\[
 N_e^2>1+49r^2/64+7r/8,\qquad
 D^2<1+r^2-r.
\]
Their difference exceeds \(r(15/8-15r/64)>0\).
For \(.16\le x\le.22\), they instead give
\[
 N_e^2>1+49r^2/64+21r/50,\qquad
 D^2<1+r^2-9r/25<2.
\]
The difference exceeds
\[
 r(39/50-15r/64)>r/2,
\tag{10}
\]
because \(r<23/20\) and \(69/256<7/25\).
Thus every retained regular cap profile is increasing in \(x\).

If \(c>0\), then \(r>1\) and (10) further gives
\[
       \partial_x\{\Re\Xi_0+\lambda\}>
                      \tfrac12\log(5/4)>1/9
                  \quad(.16\le x\le.22).
\tag{11}
\]
The positive atanh series proves the last inequality.
Transport across that interval saves more than
\[
                         (.22-.16)/9=1/150.
\tag{12}
\]
The extra physical right-row allowance in the complete cap is less
than \(1/200\), and occurs only for \(c>0,x<.16\).
Its underlying right-cut profile has \(R=1\), so (12) pays it
with reserve \(1/600\). Further transport to smaller \(x\) is
favorable. When \(c\le0\), or \(x\ge.16\), the allowance is zero.

The true-cap-end profile is
\[
                  E_{\rm end}(c)=3/5+2\pi c_++(\log4)/100.
\tag{13}
\]
Both it and \(\lambda\) are independent of \(x\). Its transport
is therefore exact and requires no regular-profile derivative.

At \(x=.22\), the completed cap-plane theorem controls every
cap profile and both true ends. The completed typed last-row
comparison controls \(\lambda\), including all revived carriers,
by the original ordinary plane. The actual attached and ordinary
input domains are precisely those used by the three-row source
assembly, including the length-three word. Adding the planes
cancels their first slopes and leaves \(\Gamma-2\gamma_*\).
Equations (8)--(13) transport this calibration to (1), proving
(7). No numerical last-row margin or finite last-row value is used.
\(\square\)

The same proof, with zero-safe row bounds, controls the full reflected
late tail. Indeed the original reflection lemma gives
\[
                 E_0(s)\le E_0(1)=\lambda
                      \quad(1-x\le s\le1),
\tag{14}
\]
since \(x\le z\). Thus every physical row from
\(\lceil N(1-x)\rceil\) through \(N-1\) is included.

## 3. A further wrapped block decreases to its paid endpoint

For real \(s=1-v\), put
\[
 N_s=|1-r e^{2\pi i(v-x)}|,\quad
 N_b=|1-t e^{-2\pi i(z-v)}|,\quad Q=2\sin\pi v.
\]
The original exponentiated row derivative is
\[
                   e^{\partial_sE_0}=\frac{N_sN_b}{rQ^2}.
\tag{15}
\]
Suppose \(1/3\le v\le z\le9/20\). Then
\(0\le z-v\le7/60\), \(Q^2\ge3\), and (2) gives
\[
\begin{split}
 N_b^2&=(1-t)^2+4t\sin^2\pi(z-v)\\
 &<\frac{121}{400}+\frac{31}{5}\left(\frac{11}{30}\right)^2
   =\frac{20449}{18000}<\left(\frac{16}{15}\right)^2 .
\end{split}
\tag{16}
\]
Here \(\sin y\le y\) and \(\pi<22/7\) suffice.
Since \(N_s\le1+r\),
\[
             \frac{N_sN_b}{rQ^2}
              <\frac83\frac{16}{15}\frac13
                         =\frac{128}{135}<1.
\tag{17}
\]
At a zero numerator, the one-sided logarithmic limit has the same
direction. The complete continuous row rate therefore decreases
with \(s\) on
\[
                         1-z\le s\le2/3,
\tag{18}
\]
whenever \(z\ge1/3\). It is bounded there by the endpoint
\(E_0(1-z)\), already paid with the complete cap by the unwrapped
theorem. No critical-root selection is needed for (17)--(18).

Define
\[
                         s_L(z)=\max(2/3,1-z).
\tag{19}
\]
Combining (18) with the adopted unwrapped block pays every continuous
rate from \(s=1/2\) through \(s=s_L(z)\), with every complete-cap
profile and its possible allowance.

## 4. The literal finite outer-row blocks

**Theorem 2.** For every \(\tau>0\), both level parities satisfy
\[
\begin{split}
 |U_{0,N}(w,X)|
 \bigg\{&
 \sum_{j=\lceil N/2\rceil}^{\lfloor Ns_L(z)\rfloor}|R_{j,N}(a,b)|
 +\sum_{j=\lceil N(1-x)\rceil}^{N-1}|R_{j,N}(a,b)|
 \bigg\}\\
 &\le C_\tau N^{A_\tau}
                    e^{N\{\Gamma(z)-\gamma_*+\tau\}}.
\end{split}
\tag{20}
\]
This holds on a sufficiently small fixed ordinary-color neighborhood
of \(w=-2\), with the same rate for every fixed derivative of the
cap in that color on a smaller neighborhood.

For the first block, use the unwrapped theorem and (17)--(19).
For the last block use Lemma 1 and (14). The original zero-safe
finite-product estimate applies uniformly at every physical index,
including the rounded boundaries and all numerator zeros. It
bounds each row by its continuous rate plus a prescribed arbitrarily
small tolerance and an \(N\)-polynomial. Summing at most \(2N\)
rows changes only that polynomial. This proof compares rates,
not finite values at possibly zero half- or last-index factors.

The complete cap bounds hold on the whole real ordinary-color
interval, after discarding the favorable angular loss in the
regular profiles and retaining the separate true-end term.
The cap has degree less than \(N\). Interval polynomial continuation
and Cauchy's formula therefore give the stated fixed-color
neighborhood and derivatives with an arbitrarily small additional
rate cost. No color-independent factor is divided out.
All signs, finite stops, both parities and original external
normalization remain unchanged.

## 5. The true cap ends when \(c\le0\)

There is an additional estimate that is separate from the regular
profiles. Let \(G_H\) be the original radial primitive of the
reflection theorem, and let
\(\Phi(v)=E_0(1-v)-E_0(1)\).
For \(0\le v\le z\), the centered first arc and the monotone second
arc give
\[
                  \Phi(v)\le h(v)-\lambda v,\qquad
                  h(v)=J(v)-2J(v/2).
\tag{21}
\]
Both arcs lie in their original period; \(0\le v\le z\le.45\).
For the first, an even increasing integrand has its smallest
integral on the centered interval, giving \(-2G_{|c|}(v/2)\).
For the second \(v\le z\) gives \(-G_{|d|}(v)\).
Using \(G_H\ge J\) proves (21).

The all-angle leg lemma, with the drift retained, also gives
\[
                 E_0(1-v)-E_0(1/2)\le\lambda(1/2-v).
\tag{22}
\]
Consequently
\[
\begin{split}
 E_0(1-v)-\max\{E_0(1/2),E_0(1)\}
 &\le \min\{h(v)-\lambda v,\lambda(1/2-v)\}\\
 &\le(1-2v)h(v)\le\frac{\log2}{8}<\frac7{80}.
\end{split}
\tag{23}
\]
For the middle inequality, take the convex combination with
weights \(1-2v\) and \(2v\); its two drift terms cancel.
For the last one,
\[
 h'(v)=\log(2\cos(\pi v/2))\le\log2,\quad h(0)=0,\quad
 v(1-2v)\le1/8.
\]
The elementary bound \(\log2<7/10\) follows, for example, from
the first five positive terms of \(e^{7/10}>2\).
This is an upper bound for possible interior overshoot, not an
endpoint-only ordinary theorem.

Assume now \(c\le0\). The true-cap-end rate (13) is below \(123/200\),
whereas the original bare cap plane at \(x=.22\) exceeds \(79/100\).
Thus its reserve is greater than \(7/40\).
Both its joint half-row and last-row endpoints retain this reserve
below \(\Gamma-2\gamma_*\) at that comparison point.
The last combination is independent of \(x\). For the half combination,
\[
 \partial_x\{E_{\rm end}+E_0(1/2)\}
 =\log\frac{|1+r e^{-2\pi ix}|}{|1-r e^{-2\pi ix}|}>0,
\tag{24}
\]
because \(x<1/4\). They therefore retain the same reserve at every
early target. Combining (23) with that reserve proves that the
true-end term of the cap majorant, multiplied by every wrapped
row with \(v\le z\), has rate less than
\[
                         \Gamma(z)-2\gamma_*-\frac7{80}.
\tag{25}
\]
For \(v\ge z\), its rate is already bounded in the unwrapped proof,
which explicitly retains the true-end profile. Hence the entire
high block of this true-cap-end term is paid when \(c\le0\),
with the finite, parity and color scope of (20).
No such additional true-end assertion for \(c>0\) is made here.

## 6. The precise remaining interior

After (20), the only remaining high physical rows lie between its
two displayed finite blocks. Their continuous interval is
\[
 s_L(z)<s<1-x,\qquad
               x<v=1-s<\min(z,1/3).
\tag{26}
\]
At a stationary row,
\[
                         N_sN_b=rQ^2.
\tag{27}
\]
For any regular cap profile its joint transport derivative is
\[
                     \partial_x H_e=\log(N_eN_s/D^2).
\tag{28}
\]
The already proved comparison \(N_e>D\) holds for every original
profile, including the lower alias before its optional domination.
Furthermore
\[
 N_s^2-D^2=
            4r\{\sin^2\pi(v-x)-\sin^2\pi x\}.
\tag{29}
\]
In (26), \(v\ge2x\) makes (29) nonnegative. Thus a stationary
regular profile with a nonpositive derivative (28) must satisfy
\[
                         x<v<\min(2x,z,1/3).
\tag{30}
\]
This is a restriction on possible unproved maxima, not a selection
of them.

For clarity, put \(q=\cot\pi v=-\cot\pi s\),
\(A=\cot\pi a\), \(B=\cot\pi b\). The original stationary test is
\[
 P(q)=e^{2\pi(d-c)}|\sin\pi a\,\sin\pi b|^2
                         |q-A|^2|q-B|^2,\qquad
                         P(q)=1,\quad P'(q)\le0.
\tag{31}
\]
These descending level-one crossings have not been excluded or
calibrated in (30). Likewise, excluding interior joint maxima
would not by itself calibrate the fixed-height boundary \(x=.1\);
that face remains explicit. The true-end profile has a different
joint derivative and is separate when \(c>0\).

The result is a complete finite bound on the two indicated high-row
blocks, and an additional true-end statement in its stated height
class. The remaining regular interior prevents a full first33
early-pair conclusion outside previously covered sign classes.
There is no new whole-word, signed lower-bound, closed-knot or
short-partial-filling theorem.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_unwrapped_stationary_high_row_transport.md | 24210764f62ef04250a63dbcb5b5e82d4bdf59ede7eacb88889e5318dfc4d4aa |
| research_mixed_early_three_positive_private_central.md | d7f54fc0a20c5ccce15b028d16dbcaee2ef0eefbea70795089da097c9730635e |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_first_cap_plateau_completion.md | 4b1a55000a114835ce4b2868b79f4bec63ee781d6d997f7fa6b37f7896e4e87d |
| research_mixed_three_row_source_assembly.md | 947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |

All directly used source statements and proof portions were read.
Only written inequalities are used. No mathematical numerical
evaluation, saved-value arithmetic, import, compilation, test or
frozen-source edit was performed.

