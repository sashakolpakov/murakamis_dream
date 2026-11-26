# Paying both end ranges of the far-half conditional source

Research deduction, 7 November 2026. On the remaining real part of
the first-coordinate complement, every conditional row at or beyond
the wall \(a+t=1\) has a strict selected-source gap. The initial
rows \(0\le t\le1/16\) have a separate strict gap. Both bounds
persist in fixed real collars and on short vertical cut segments.
The remaining finite conditional sum can therefore use two cuts
strictly inside the original regular factorial chart. This does not
estimate its central zero mode or the rest of its side currents.

## 1. The literal rows and their real upper profile

Keep the exact cap \(U_{0,N}\) and conditional polynomial
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                   \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},
 \quad p_j(X)=(rX;r)_j,\quad P_j=(r;r)_j,\quad
                 r=e^{-2\pi i/N}.                           \tag{1}
\]
Take
\[
       \frac12\le a\le\frac{13}{16},\qquad
       X=e^{-2\pi ia},\qquad v=1-a\in[3/16,1/2].
                                                               \tag{2}
\]
No row of (1) is set to zero because \(a+j/N\ge1\).
At a nonphysical \(a\), such a row can be nonzero.

Use the continuous periodic primitive \(J\), and define
\[
 \begin{split}
 I_a(t)&=J(a+t)-J(a),\\
 L(t)&=-2J((1-t)/2),\\
 F_a(t)&=L(t)+I_a(t)-3J(t),\qquad 0\le t\le1.
 \end{split}                                                 \tag{3}
\]
The whole-index numerator estimates in
[the continuous far-half cap theorem](research_mixed_three_four_continuous_far_half_cap.md)
and the polynomial maximum principle give, uniformly in (2),
\[
 \sup_{|Y|\le1}
 \left|\frac{X^{-j}p_j(X)p_j(Y)}{P_j^3}\right|
       \le C_\tau N^{B_\tau}e^{N\{F_a(j/N)+\tau\}}.
                                                               \tag{4}
\]
The chirp has modulus one because \(a\) is real. The estimate
retains every product zero and the two extreme physical indices.

## 2. All rows beyond the wall have rate less than \(7/15\)

**Lemma 1.** On (2),
\[
                  F_a(t)<7/15\qquad(v\le t\le1).
                                                               \tag{5}
\]

*Proof.* Put \(B_v(t)=I_{1-v}(t)-J(t)\). Periodicity and
oddness of \(J\) give
\[
 B_v(t)=J(t-v)+J(v)-J(t),\qquad B_v(v)=B_v(1)=0,
 \quad
 B_v'(t)=\log\frac{\sin\pi(t-v)}{\sin\pi t}
                       \quad(v<t<1).
                                                               \tag{6}
\]
The difference of the two squared sines in (6) is
\(-\sin\pi v\,\sin\pi(2t-v)\). Thus \(B_v\) decreases from
\(t=v\) to \(t=(1+v)/2\), then increases to \(t=1\).
Its logarithmic endpoint singularities are integrable, and both
endpoint values are zero. It follows that
\[
 B_v(t)\le0\quad(v\le t\le1),\qquad
              F_a(t)\le L(t)-2J(t).
                                                               \tag{7}
\]
The existing whole-index bound
\(\max_{[0,1]}[L(t)-2J(t)]<7/15\) proves (5) on the entire
interval. This quotient comparison in fact holds for every
\(0<v\le1/2\); the lower bound \(v\ge3/16\) will keep a
nonempty regular central interval below the wall. \(\square\)

Let \(C_{1,N}^{\mathrm{wall}}(X,Y)\) denote the literal sum in
(1) over \(j/N\ge1-a\). Its whole-disk bound follows by
summing the positive estimates (4)--(5). The complete coherent
cap bound is
\[
 |U_{0,N}(w,X)|\le C_\tau N^{B_\tau}
                     e^{N(1549/1500+\tau)}.
                                                               \tag{8}
\]
Its all-real version is part of
[the complementary real-color theorem](research_mixed_three_four_complementary_real_colors.md).
It retains the complete endpoint polynomials and every private row.
Consequently
\[
 \sup_{|Y|\le1}
 |U_{0,N}(w,X)C_{1,N}^{\mathrm{wall}}(X,Y)|
 \le C_\tau N^{B_\tau}e^{N(2249/1500+\tau)}.
                                                               \tag{9}
\]
The gap below \(77/50\) is \(61/1500\). Equation (9)
is an upper bound on the complete sum of the absolute row
contributions after the coherent cap has been bounded; it also
controls any subset of these rows.

The lower end also admits a whole-row estimate, without invoking
a conditional saddle.

**Lemma 2.** Uniformly on (2),
\[
                F_a(t)<77/160\qquad(0\le t\le1/16).
                                                               \tag{9a}
\]

*Proof.* Each real incoming factor has modulus at most two, so
\(I_a(t)\le t\log2\). The centered-arc integral likewise
satisfies \(L(t)\le t\log2\). Concavity of sine on
\([0,\pi/6]\) gives \(2\sin\pi s\ge6s\), whence
\[
 J(t)\ge t\{\log(6t)-1\},\qquad
 F_a(t)\le f(t):=t\{3+2\log2-3\log(6t)\}.
                                                               \tag{9b}
\]
The value at zero is interpreted continuously. Since
\(f'(t)=2\log2-3\log(6t)>0\) on \((0,1/16]\),
\[
 f(t)\le f(1/16)
   =\frac{3+11\log2-3\log3}{16}<\frac{77}{160}.
                                                               \tag{9c}
\]
Here \(\log2<7/10\) and \(\log3>1\); the latter follows
already from the positive exponential series bound \(e<3\).
This proves (9a). \(\square\)

Combining (4), (8), and Lemma 2, the complete sum over the
physical rows \(j/N\le1/16\), including \(j=0\), has product
rate
\[
 \frac{1549}{1500}+\frac{77}{160}
       =\frac{18167}{12000}
       =\frac{77}{50}-\frac{313}{12000}
                                                               \tag{9d}
\]
on the entire outgoing unit disk. The complete coherent cap is
still the one in (8).

## 3. Fixed paid collars and two regular cuts

The function \(F_a(t)\) in (3) is jointly continuous on the
compact real domain (2), \(0\le t\le1\), including the wall.
This follows either from the periodic primitive or from the
uniform integrability of its logarithmic singularities.
Lemma 1 and compactness imply that there is a fixed
\(0<\varepsilon<1/64\), independent of \(N\), such that
\[
 F_a(t)<\frac7{15}+\frac1{100}
       \quad\hbox{whenever }t\ge1-a-2\varepsilon .
                                                               \tag{10}
\]
For example, a sequence violating every shrinking collar would
have a convergent subsequence with \(t\ge1-a\), contradicting
(5). This is an existence proof from a strict analytic bound,
not a sampled continuity assertion.

The full conditional rows in this collar, including every row
past the wall, therefore satisfy the whole-disk product bound
\[
 |U_{0,N}C_{1,N}^{\mathrm{collar}}|
 \le C_\tau N^{B_\tau}
         e^{N\{2249/1500+1/100+\tau\}}.
                                                               \tag{11}
\]
Here \(C^{\mathrm{collar}}\) can mean any subset of the indicated
physical rows. Since
\[
 \frac{77}{50}-\frac{2249}{1500}-\frac1{100}
                         =\frac{23}{750}>0,                 \tag{12}
\]
the common tolerance can be chosen so that (11) has rate
strictly below \(77/50\).

At the lower end, the same compact continuity gives a fixed
\(\varepsilon_->0\) such that
\[
 F_a(t)<\frac{77}{160}+\frac1{100}
                  \quad(0\le t\le1/16+\varepsilon_-).
                                                               \tag{12a}
\]
Both end collars, with any subsets of their physical rows, have
the common whole-disk cap-times-conditional ceiling
\[
 \frac{18167}{12000}+\frac1{100}
       =\frac{77}{50}-\frac{193}{12000}.
                                                               \tag{12b}
\]
Thus finite tolerances leave a strict reserve below \(77/50\)
for either collar or their union.

For a concrete remaining finite sum, put
\[
 K_N(a)=\lceil N(1-a-\varepsilon)\rceil,\qquad
 \sigma_{+,N}(a)=\frac{K_N(a)-1/2}{N},\qquad
 L_N=\lfloor N/16\rfloor+1,\quad
 \sigma_{-,N}=\frac{L_N-1/2}{N}.
                                                               \tag{13}
\]
For all sufficiently large \(N\),
\[
 1-a-\frac54\varepsilon
  <\sigma_{+,N}(a)
  <1-a-\frac34\varepsilon,\qquad
                 L_N<K_N(a)<N.
                                                               \tag{14}
\]
Deleting all \(j\ge K_N(a)\) is licensed by (10)--(12).
Deleting \(j<L_N\) removes exactly the initial physical rows
\(j/N\le1/16\), already paid in (9d). The lower half-grid
cut differs from \(1/16\) by at most \(1/(2N)\), so for
large \(N\) it belongs to the fixed paid collar (12a).
The central interpolation for the remaining indices
\(L_N\le j<K_N(a)\) is exactly
\[
 T_N(s;a,y)=e^{2\pi iNas}\,
   \Pi_N(a+s)\Pi_N(y+s)E_N(a)E_N(y)E_N(s)^3.
                                                               \tag{15}
\]
The notation \(\Pi_N\) is the original numerator factorial and
\(E_N\) its reciprocal. Exact recurrence gives
\[
 T_N(j/N;a,y)=X^{-j}p_j(X)p_j(Y)/P_j^3,\qquad
                         Y=e^{-2\pi iy}.                    \tag{16}
\]
This is the same conditional interpolation already used in the
ordinary source proofs.

For the selected target \(y\in P+i/100\), the whole vertical
rectangle
\(\sigma_{-,N}\le\Re s\le\sigma_{+,N}(a)\) has
\[
 0<\Re s<1/2,\qquad
 0<\Re(a+s)<1-3\varepsilon/4,\qquad
                     0<\Re(y+s)<.95.                       \tag{17}
\]
The upper strict bound for the first numerator uses (14);
the lower bounds and the second upper bound hold uniformly for
large \(N\). The fixed parameters \(a,y\) also have real parts
strictly between zero and one. Thus every factor in (15) stays
in its original regular strip for any fixed finite heights.
The holomorphic numerator extension across positive walls in
[the joint global chart](research_mixed_fourier_right_cap_joint_global_chart.md)
already justifies the undeleted full source; no new extension
or logarithmic lift is needed for the retained rectangle (17).

If \(\mathcal R_N\) is any such rectangle with its lower side
below and upper side above the real axis, the exact source is
\[
 \sum_{j=L_N}^{K_N(a)-1}T_N(j/N;a,y)
   =\frac1{2\pi i}\int_{\partial\mathcal R_N}
                    T_N(s;a,y)\,\pi N\cot(\pi Ns)\,ds .
                                                               \tag{18}
\]
Its usual zero mode, horizontal aliases and cut currents are
therefore all retained. The moving cut in (13) is a half-grid
cut. Equation (18) is a pointwise identity for every real \(a\);
its finitely many changes of index range do not change the
literal decomposition of the complete finite polynomial.

## 4. Calibration and the remaining currents

Use precisely the ordinary-next reference family and selected
target of
[the filtered selected-plateau theorem](research_mixed_next_filtered_selected_plateau.md):
\[
 y=x+i/100,\ x\in P,\qquad
 z=u+i\Im z_*,\ u\in P,\qquad Z=e^{-2\pi iz},\quad
                      \beta\in\{0,1\}.
                                                               \tag{19}
\]
Every end-collar polynomial has degree at most \(N-1\) in \(Y\).
Its whole-disk bound (11)--(12b) supplies the only prefix input
used by Sections 3--4 of that theorem. Applying that comparison
therefore gives
\[
 \begin{split}
 &|U_{0,N}(w,X)C_{1,N}^{\mathrm{collar}}(X,Y)
              d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|
                              |d_N(Z)|^{\beta/2}\\
 &\qquad\le C_\tau N^{B_\tau}
               e^{N\{\Lambda_{123}(z)-1/500+\tau\}} .
 \end{split}                                                 \tag{20}
\]
This is the original full third factor and actual first-pair
tangent, for both next types and all real ordinary colors.
Both Fourier-weight alternatives remain; when \(\beta=0\),
no outgoing weight is inserted. It leaves finite loss \(1/1000\)
after tolerances and polynomial factors.

The real values of both cuts in (15) have the same profile
bounds: (14) places the upper one inside (10), and (13) places
the lower one inside (12a). For the selected outgoing
radius, its numerator integral has the upper bound
\(L(s)+2\pi s/100\), no larger than \(L(s)+\pi/50\).
To prove this for a continuous real index \(t<1/2\), put
\(R=e^{2\pi/100}\) and use
\[
 \log|1-Re^{i\theta}|
       =\log R+\log|1-R^{-1}e^{i\theta}|.
                                                               \tag{21}
\]
The maximal arc integral of the second term, among arcs of
length \(2\pi t\), is centered at \(\theta=\pi\): the integrand
is symmetric there and decreases with angular distance from that
center. On that centered arc \(\cos\theta\le0\), so
\(|1-R^{-1}e^{i\theta}|\le|1-e^{i\theta}|\).
Integration therefore gives \(L(t)+t\log R\), including
noninteger \(Nt\). This is a continuous factorial-phase bound,
not an inference from the degree of a physical row polynomial.
This is exactly the radius allowance in the selected-plateau
comparison. Uniform continuity of the regular phase on (17)
then supplies a fixed \(\eta_0>0\) such that both portions
\(\sigma_{\pm,N}+i[-\eta_0,\eta_0]\) have the same strict
calibrated gap, after an additional small common tolerance.
The compact real-part distance from \(a+s=1\) is at least
\(3\varepsilon/4\), uniformly in \(a,N\); all other factorial
arguments in (17) also have fixed compact margins. Thus this
phase-continuity assertion is uniform at both cuts.
The ordinary cut kernels on a half-grid vertical line have
bounded modulus; their factors \(N\), and the length of the
short joins, cost only polynomial powers. This pays both short
cut currents as actual currents of (18).

The all-real and local fixed-derivative conclusions follow as
in the selected-plateau proof: Markov is applied to complete cap
coefficients before summation, and Cauchy is applied on smaller
fixed parameter neighborhoods. The row ranges and the integration
segments are held fixed when differentiating the outside
parameters. The integer cut depends only on the first contour
coordinate \(a\), not on the ordinary color or the outgoing
parameters. The original contour densities still carry their
factors \(N\).

Equations (18)--(20) do not pay the retained central zero mode
or the rest of either long vertical alias.
The initial vertical first-coordinate connector is also outside
this theorem. The result removes the positive-wall obstruction
from the remaining real-arc conditional chart, and pays its lower
physical end, by bounding complete finite rows rather than discarding
an off-grid continuation.
