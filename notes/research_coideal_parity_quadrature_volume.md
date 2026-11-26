# Exact finite quadrature extends the signed coideal volume chamber

24 November 2026. Research note. Written proof.

The actual mixed coideal coefficient has an exact positive quadrature
on a specified index parity. Its finite zero strings annihilate every
sample outside the common negative gap. This replaces the global
absolute-integral comparison in C by exact finite orthogonality.
Consequently the signed coefficient has the sewn octahedral volume
rate throughout the cooriented domain on that parity, including points
outside C's discriminant chamber.

The assertion concerns the full actual local coefficient, with its
quadratic height phase and both neighboring metric weights. It does
not place an arbitrary geometric character or original marked closing
in the stated channels.

## 1. Exact source data and statement

Use the complete physical conventions of C and T:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \delta=\pi/N,\quad \sqrt q=e^{\pi i/(2N)},\quad
 \kappa=e^{i\pi d^2/(2N)},\qquad
 F_a=\prod_{j=1}^a(1-Q^j),\quad F_0=1,\quad F_d=N.
 \tag{1}
\]
Sort the simple coideal roots by
\[
 \lambda_r=2\sqrt q\cos\alpha_r,\qquad
 \alpha_r=(r+\tfrac12)\delta,\qquad 0\le r\le d.
 \tag{2}
\]
The complete continuants and finite polynomials are
\[
 D_{-1}=0,\quad D_0=1,\qquad
 D_{a+1}(\lambda;\sigma)
 =(\lambda+qQ^a\sigma)D_a(\lambda;\sigma)
                  -q(1-Q^a)^2D_{a-1}(\lambda;\sigma),
 \qquad
 \Phi_{rs}(z)=\sum_{a=0}^d
                   \frac{D_a(\lambda_r;\lambda_s)}{F_a}z^a.
 \tag{3}
\]
In particular all endpoint arrows and the original crossing scalar
are fixed. For two pairs of indices write
\[
 \Sigma_N=\sum_{a=0}^d
   \frac{\overline{D_a(\lambda_{r_1};\lambda_{s_1})}
                    D_a(\lambda_{r_2};\lambda_{s_2})}{|F_a|^2}.
 \tag{4}
\]
Assume cross-coorientation and the following index parity:
\[
 r_i+s_j\le N-2\quad(1\le i,j\le2),\qquad
 R=\max(r_1,r_2),\quad S=\max(s_1,s_2),\qquad
                         N+R+S\ \hbox{is even}.
 \tag{5}
\]
Cross-coorientation is equivalently
\(\cos\alpha_{r_i}+\cos\alpha_{s_j}>0\) for every pair.
The parity in (5) depends on the selected indices as well as the level.
Put
\[
 f_r=\exp\{i\delta r(r+1)/4\},\qquad
 \gamma_{rs}=e^{i\pi d/4}f_r/f_s ,
 \tag{6}
\]
and choose \(p\in\{0,1\}\) congruent to \(1-R\), equivalently
to \(N+S-1\), modulo two. Define
\[
 M=\frac{N-R-S}{2}\ge1,\qquad
              k_a=-N+S+1+2a\quad(0\le a<M).
 \tag{7}
\]

**Positive quadrature theorem.** At every level and every quadruple
satisfying (5),
\[
 \boxed{\quad
 \Sigma_N=\overline{\gamma_{r_1s_1}}\gamma_{r_2s_2}J_N,\qquad
 J_N=\frac1N\sum_{a=0}^{M-1}
       |\Phi_{r_1s_1}(q^{k_a})\Phi_{r_2s_2}(q^{k_a})|>0 .
 \quad}
 \tag{8}
\]
No discriminant inequality is required. On compact subsets of the
cross-cooriented domain the logarithmic rate of this positive sum is
the sewn octahedral volume defined in Section 4, uniformly over the
actual roots satisfying the parity.

## 2. The exact zero intervals on both parity grids

We first record the finite product information with all endpoints.
C's exact root calculation, equivalently T's finite product, gives two
descending strings of raw zero indices, in units of \(\delta\):
\[
 N+s-1,\ N+s-3,\ldots;\qquad
 N-s-2,\ N-s-4,\ldots .
 \tag{9}
\]
If \(N+r+s\) is even, their last included indices are respectively
\(1-r,r+2\); if it is odd, these last indices are interchanged.
Their counts are \((d+h)/2,(d-h)/2\), with
\(h=s+r+1\) in the even case and \(h=s-r\) in the odd case.
These are nonnegative integers. A string with count zero is empty;
its putative upper endpoint is its lower endpoint minus two.

For completeness, these strings follow from the roots of the two
factors in T's degree-\(d\) product, or directly from
\((1-\lambda z+qz^2)\Phi(z)
=(1+q\sigma z+qQz^2)\Phi(Qz)\).
Their first points are the roots of the numerator on the right,
and successive roots advance by \(Q^{-1}\) until reaching a root
of the factor on the left. The counts just given end at the two
required left roots and total \(d\). The product has constant term
one and satisfies this equation; successive coefficients through
degree \(d\) are unique since \(1-Q^a\ne0\) for \(0<a<N\).
Thus it is the actual polynomial (3), not a limiting product.

On a chosen grid \(k\equiv p\pmod2\), the zeros of \(\Phi_{rs}\)
are exactly the step-two interval from \(L_r^p\) to \(U_s^p\), where
\[
 L_r^p=
 \begin{cases}1-r,&p\equiv1-r\pmod2,\\ r+2,&\text{otherwise},\end{cases}
 \qquad
 U_s^p=
 \begin{cases}N+s-1,&p\equiv N+s-1\pmod2,\\
               N-s-2,&\text{otherwise}.
 \end{cases}
 \tag{10}
\]
An interval is empty when its upper endpoint is its lower endpoint
minus two. The complete roots on both grids lift to
\([1-r,N+s-1]\), whose length is less than \(2N\) under (5).
Hence no zero is lost or repeated by reduction modulo \(2N\).

For the parity selected in Section 1, an \(R\)-polynomial supplies
the left endpoint \(1-R\), and an \(S\)-polynomial supplies the
right endpoint \(N+S-1\). These supplying intervals are nonempty:
their endpoint differences are respectively at least \(2R-1\)
and \(2S-1\), and are even integers, hence nonnegative.
For any two selected intervals cross-coorientation also gives
\(L_{r_i}^p\le r_i+2\le N-s_j\le U_{s_j}^p+2\).
The two nonempty extreme intervals therefore overlap or are adjacent
in the step-two grid. Their union, including any other selected
interval, is exactly
\[
 \{k:\Phi_{r_1s_1}(q^k)\Phi_{r_2s_2}(q^k)=0,\ k\equiv p\}
   =[1-R,N+S-1]\cap(p+2\mathbb Z)\quad\bmod 2N.
 \tag{11}
\]
It contains \((N+R+S)/2\) nodes. Its complement on the \(N\)-point
grid is precisely (7), ending at \(k_{M-1}=-R-1\).

All roots of both polynomials, on either parity grid, lie in the
lifted interval used in (11). Therefore every surviving node lies
in the common actual zero-free component
\(((-N+S-1)\delta,(1-R)\delta)\).
In particular the last node is not a zero: the next possible zero
is \(1-R\), two grid units later. This endpoint fact matters when
extending the phase from C's smaller safe interval.

## 3. Exact orthogonality removes every other sample

Finite Parseval on either of the two grids gives directly
\[
 \Sigma_N=\frac1N
   \sum_{\substack{k\equiv p\ (2)\\\bmod 2N}}
       \overline{\Phi_{r_1s_1}(q^k)}\Phi_{r_2s_2}(q^k).
 \tag{12}
\]
Indeed the difference of two polynomial exponents lies in
\([-d,d]\); its only multiple of \(N=d+1\) is zero.
Thus (12) is an exact unitary finite Fourier identity, with no
alias term or large-level approximation. Equation (11) annihilates
every summand except the nodes (7).

The phase at every remaining node is also exact. For a cooriented
pair the raw root lifts \(\xi\) in Section 2 satisfy
\[
 \sum\xi=\pi d/2+
       \delta\{s(s+1)-r(r+1)\}/2,\qquad
 \Phi_{rs}(e^{i\vartheta})
       =\gamma_{rs}e^{id\vartheta/2}
                                      |\Phi_{rs}(e^{i\vartheta})|
 \tag{13}
\]
on its negative zero-free component.
To check the sign, each root factor has
\(\vartheta-\xi\in(-2\pi,0)\), so its phase is
\(+i e^{i(\vartheta-\xi)/2}\).
The sum of the two arithmetic root strings is the first identity
in (13); their product phase is
\(i^d e^{-i\sum\xi/2}=\gamma_{rs}\).
This proves the formula on C's safe interval and, since there is
no intervening root, on the whole component used here.
It includes both endpoint parities and \(N=2\).

At a surviving node the factors \(e^{id\vartheta/2}\) cancel in
the mixed product. Its phase is
\(\overline{\gamma_{r_1s_1}}\gamma_{r_2s_2}\) and its magnitude
is strictly positive. Substitution in (12) proves (8).
Unwanted large peaks elsewhere on the circle have been removed by
exact zero samples. We have not bounded them by the gap maximum
or replaced the whole integral by its absolute value.

## 4. Uniform sewn-volume rate on the cooriented domain

Write \(\alpha_i=\alpha_{r_i}\), \(\beta_i=\alpha_{s_i}\),
\(a_i=\cos\alpha_i\), \(b_i=\cos\beta_i\), and put
\[
 A=a_1+a_2+b_1+b_2>0,\qquad
 x_*=\frac{a_1a_2-b_1b_2}{A},\quad \Theta_*=\arccos x_*,
 \qquad
 \psi_i=\frac{\pi-\alpha_i-\beta_i}{2},\quad
 u_i=\frac{\Theta_*-\alpha_i}{2}.
 \tag{14}
\]
Let \(\Lambda(v)=-\int_0^v\log|2\sin t|\,dt\), extended as an
odd, \(\pi\)-periodic function, and define
\[
 W_i(u)=2\{\Lambda u+\Lambda(\alpha_i+u)
                 +\Lambda(\psi_i-u)+\Lambda(\psi_i+\beta_i-u)\},
 \qquad V_{\rm sew}=\frac{W_1(u_1)+W_2(u_2)}2.
 \tag{15}
\]
Here and below compact uniformity means any compact subset of
\(\{(\alpha_1,\beta_1,\alpha_2,\beta_2)\in[0,\pi]^4:
\alpha_i+\beta_j<\pi\ \text{for all }i,j\}\).
Only the actual root quadruples with parity (5) are being estimated.

Set \(\Phi_i=\Phi_{r_i s_i}\) and use the rotated circle
\(z=q^{-1/2}e^{it}\). T's uniform log-cell comparison supplies
\[
 E_i(t)=\frac2\pi\left\{
  -\Lambda\frac{t+\alpha_i}2-\Lambda\frac{t-\alpha_i}2
  +\Lambda\frac{t+\pi-\beta_i}2
  +\Lambda\frac{t-\pi+\beta_i}2\right\},
 \quad
 \log|\Phi_i(q^{-1/2}e^{it})|^2\le NE_i(t)+C\log N.
 \tag{16}
\]
The estimate is two-sided on a fixed interior subarc of the common
gap. It is global as an upper estimate, including at zeros.
The exact finite arc has \(t+\delta\) in its last two primitive
terms; the modulus of continuity of \(\Lambda\) makes this an
\(O(\log N)\) error after multiplication by \(N\).
Thus no action constant is discarded.

Let \(E=E_1+E_2\),
\(n(x)=(x-a_1)(x-a_2)\), \(b(x)=(x+b_1)(x+b_2)\).
On \(I=(\max(-b_1,-b_2),\min(a_1,a_2))\),
\[
 n,b>0,\qquad n(x)-b(x)=A(x_*-x),\qquad
 \frac{d}{dx}\log\frac{n(x)}{b(x)}
 =-\sum_{i=1}^2\left\{\frac1{a_i-x}+\frac1{x+b_i}\right\}<0,
 \qquad
 E'(t)=\frac1\pi\log\frac{n(\cos t)}{b(\cos t)} .
 \tag{17}
\]
The endpoint signs put \(x_*\) strictly in \(I\).
Consequently \(0<u_i<\psi_i\), and \(E\) has exactly one maximum
on the closed common negative arc
\([-\pi+\max\beta_i,-\max\alpha_i]\), at \(-\Theta_*\).
It is nondegenerate, uniformly on every specified compact subset.
Integrating the log-sine primitive in (16) gives
\(E(-\Theta_*)/2=V_{\rm sew}/\pi\).
This argument uses no discriminant: it concerns the common gap,
where both \(n\) and \(b\) are positive.

The rotated surviving nodes are exactly
\(t_a=k_a\delta+\delta/2\), ranging from
\(-\pi+\alpha_S+\delta\) to \(-\alpha_R\) in steps \(2\delta\).
They all lie in the closed common continuum arc.
Thus (16)--(17) bound every summand of (8) by
\(N^C\exp(NV_{\rm sew}/\pi)\).
For large \(N\), some surviving node is within \(\delta\) of
\(-\Theta_*\). On compact subsets this node is a fixed distance
from the actual zero strings. The two-sided version of (16)
and smoothness near the maximum bound its summand below by
\(N^{-C}\exp(NV_{\rm sew}/\pi)\).
Retaining that node and averaging at most \(N\) nodes proves
\[
              \log J_N=\frac N\pi V_{\rm sew}+O_{\mathcal C}(\log N)
 \tag{18}
\]
uniformly on every compact cooriented subset.
Strict positivity in (8) itself holds at every allowed level,
independently of the sufficiently-large-level restriction in (18).

## 5. The same genuinely sewn convex octahedron

C's geometric construction needs cross-coorientation and
\(x_*\in I\), which were proved without its discriminant condition.
Here are the supporting-face checks so this extension does not
assume that separate local volume maxima sew.
Take four tetrahedra in cyclic order \(A_1,B_1,A_2,B_2\), with
their angle triples
\[
 A_i=(u_i,\psi_i-u_i,\pi-\psi_i),\qquad
 B_i=(\alpha_i+u_i,\psi_i+\beta_i-u_i,\psi_i).
 \tag{19}
\]
All angles are positive. Their common-edge angles sum to \(2\pi\).
Put
\[
 z_i=\frac{\sin u_i}{\sin(\psi_i-u_i)}e^{i(\pi-\psi_i)},\qquad
 w_i=\frac{\sin(\alpha_i+u_i)}{\sin(\psi_i+\beta_i-u_i)}e^{i\psi_i},
 \qquad
 \rho_i=-\frac{x_*-a_i}{x_*+b_i}>0.
 \quad z_iw_i=-\rho_i,\qquad \rho_1\rho_2=1 .
 \tag{20}
\]
The last equality is precisely \(n(x_*)=b(x_*)\). Thus the
shapes close in modulus and argument. With poles \(0,\infty\),
their equatorial vertices are \(1,z_1,-\rho_1,-\rho_1z_2\).
Their argument increments are
\(\pi-\psi_1,\psi_1,\pi-\psi_2,\psi_2\), all in \((0,\pi)\).
They form a simple star-shaped quadrilateral.

At the pole \(\infty\), its two interior-half link angles are
\(\psi_i+\alpha_i\); the joins are
\((\pi+\beta_1-\alpha_2)/2\) and
\((\pi+\beta_2-\alpha_1)/2\).
The join formula follows from
\(u_1-u_2=(\alpha_2-\alpha_1)/2\).
All four angles lie in \((0,\pi)\), so the quadrilateral is
strictly convex and its four vertical side planes support.
At zero use the Möbius map \(z\mapsto-1/z\).
The reciprocal link has interior-half angles \(\psi_i+\beta_i\)
and joins \((\pi+\alpha_1-\beta_2)/2\),
\((\pi+\alpha_2-\beta_1)/2\), again in \((0,\pi)\).
Its ordered arguments and these angles give the other four
supporting planes. Hence the four positive tetrahedra fill the
convex ideal octahedron bounded by all eight supporting faces.

Their ordinary tetrahedral volumes sum to (15); the opposite
\(\Lambda(\psi_i)\) terms cancel within each half.
Thus the action in (18) is the volume of this one sewn octahedron.
No independent maximization of the two halves was used.

## 6. Actual signed crossing coefficients and scope

For an actual same-frame face let the input, output, external and
deeper sorted indices be \(r,r',v,s\). Apply the theorem to
\((r_1,s_1)=(r,v)\), \((r_2,s_2)=(r',s)\).
When its cross-coorientation and index parity hold, C's exact
inverse-row and central-coefficient identities give
\[
 B^+_{r',r}=(-1)^{r'}\sin\alpha_{r'}
          \frac{f_vf_s}{f_{r'}f_r}J_N,\qquad
 B^-_{r',r}=\overline{B^+_{r',r}} .
 \tag{21}
\]
The scalar has not been discarded:
\(\kappa q^{d/2}i^{-d}=1\) with the lift (1), since \(d+1=N\).
C's separate symmetry in the two middle and two neighboring
labels shows that both signs have this same positive amplitude.
The sine factor and its inverse have polynomial size. Therefore
both actual entries have rate (18).

For clarity define
\(\nu=\lambda_v,\lambda=\lambda_r,\lambda'=\lambda_{r'},
\sigma=\lambda_s\), and
\(h_N(\xi,\zeta)=\sum_{a=0}^d|D_a(\xi;\zeta)/F_a|^2\).
In the complete nested physical joint Haar frame the additional
positive normalization is exactly
\[
 \left[\frac{h_N(\nu,\lambda')h_N(\lambda',\sigma)}
              {h_N(\nu,\lambda)h_N(\lambda,\sigma)}\right]^{1/2}.
 \tag{22}
\]
Both incident edges are retained. T's uniform two-label volume
profile gives the same four-term volume correction as C(36).
The removed-head tail-pair form is a different normalization.
None of these full finite changes removes a Casimir normal channel.

The other index parity is not settled by this argument.
For the parity proved here no comparison with the whole
absolute-circle integral is asserted outside C's original chamber.
The theorem instead evaluates the signed coefficient by an exact
positive sampled sum, even when additional absolute-value peaks
occur away from its supporting samples.

The original input, marked closing and external scalar \(\chi_N\)
must still be retained in any assembled word. The argument does
not show that all intermediate channels lie in this domain, that
the resulting face phases align with those boundaries, or that an
arbitrary coherent closed sum has a lower bound.
No global cycle, new finite-exception theorem or knot-volume
identity follows from the local result.

Finite Fourier orthogonality and log-cell estimates are elementary
or already available in T and C. The additional statement is the
source-specific root-support identity (11), its exact positive
quadrature, and the resulting removal of the discriminant
restriction on the specified parity.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| C | [Signed coideal volume chamber](research_coideal_crossing_signed_volume_chamber.md) | 634 | 7bf6fb943d2c8080875375c4529776159fc72fbde2e5d8a7d0742e0cbdb10fc0 |
| T | [Exact coideal crossing transport](research_coideal_crossing_orthogonality_transport.md) | 595 | 4555fecc6377077dbdc4cfb3afac50f09d180efc5659716bac8497319310114c |

Only written mathematics, complete source reads and text/hash operations
were used. Earlier final notes, public manuscripts and the ledger are unchanged.
