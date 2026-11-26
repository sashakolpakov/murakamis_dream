# Positive Fourier bounds for a connected subtree with zero crossing powers

Research lemmas, 2 November 2026. The positive Fourier argument for a
single zero-power vertex has a multivariate version. It gives a bound
for all low Newton indices, with every Fourier charge included, and
suppresses the low indices outside an interior saddle neighborhood.
Two further questions remain: existence of the required coupled saddle
and control of high indices. The first already fails in the regular
interior chart for two adjacent trivalent vertices. Thus these lemmas
do not assert a boundary asymptotic for every connected subtree.

## 1. The original polynomial

Let \(S\) be a nonempty connected proper set of vertices in a fixed
finite tree. Write \(k=|S|\), let \(E_S\) consist of the internal
edges and the edges joining \(S\) to its complement, and put
\(m=|E_S|\). Each boundary edge has a distinct outside endpoint,
whose angle is denoted by \(u_e\). All crossing powers at vertices
in \(S\) are zero.

Use the Newton polynomials and full closing functional
\[
 e_a(z)=S_a^{-2}\prod_{j<a}(2\cos((2j+1)\pi/N)-z),\qquad
 S_a=\prod_{r=1}^a2\sin(\pi r/N),
 \tag{1}
\]
\[
 P_N(z)=\prod_{j=0}^{N-1}
       (z-2\cos((2j+1)\pi/N)),\qquad
 \phi_N(f)=(-1)^{N-1}N^2[z^{N-1}]\operatorname{rem}_{P_N}f.
 \tag{2}
\]
Thus a double root retains its first derivative. Define
\[
 K_N(t,u)=\sum_{a=0}^{N-1}e_a(-2\cos t)e_a(-2\cos u).
 \tag{3}
\]
The original source polynomial of the selected subtree is
\[
 Z_{S,N}(\mathbf u)=
 \left(\prod_{v\in S}\phi_N^{(v)}\right)
 \left[
  \prod_{vw\ {\rm internal}}K_N(t_v,t_w)
  \prod_{e=vw\ {\rm boundary},\,v\in S}K_N(t_v,u_e)
 \right].
 \tag{4}
\]
Here \(\phi_N^{(v)}\) acts in the spectral variable \(-2\cos t_v\).
Before applying the traces, the polynomial is kept at its actual
degree, which can exceed \(N-1\) in a selected variable.

An edge index is low if \(2a<N\) and high otherwise.
Let \(Z^{\rm low}_{S,N}\) be (4) with every edge index low.
For an arbitrary set \(\mathcal A_N\) of all-low edge assignments,
write \(Z^{\mathcal A}_{S,N}\) for the corresponding partial sum.
The set may include simultaneous restrictions on several indices.

## 2. Positivity in the full quotient and the high-index support

The exact product rule is
\[
 e_i e_j=
 \sum_{r=\max(i,j)}^{i+j}
 \frac{S_{i+j}S_r}
      {S_iS_jS_{r-i}S_{r-j}S_{i+j-r}}e_r
 \quad(i+j<N);
 \qquad e_i e_j=0\quad(i+j\ge N).
 \tag{5}
\]
All displayed coefficients are positive. The zero in the second
case is a full quotient identity: the product is divisible by \(P_N\)
with its root multiplicities. The derivation and the direct trace
pairing are given in
[the degree-three tail proof, Section 2](research_degree_three_zero_wire_tails.md#2-exact-positivity-including-the-double-root-derivatives).

Iterating (5) shows that the quotient representative of any product
of basis elements has nonnegative Newton coefficients. Since
\(\phi_N(e_r)=\mathbf1_{r=N-1}\), it follows that
\[
 \phi_N\left(\prod_{e\ni v}e_{a_e}\right)\ge0
 \tag{6}
\]
for every fixed index assignment and every selected vertex.
Associativity ensures that the conclusion does not depend on the
order used to multiply the factors.

If two high indices meet a selected vertex, their sum is at least
\(N\), and (5) makes the whole vertex factor zero. Consequently a
nonzero assignment can have at most one high edge at each selected
vertex. In particular, its internal high edges form a matching;
a high boundary edge also excludes every other high edge at its
selected endpoint. This statement does not discard a normal
derivative.

For a low index the exact Laurent formula
\[
 e_a(-2\cos t)=
 \frac{S_{2a}}{S_a^2}
 \sum_{r=-a}^a\frac{e^{irt}}{S_{a+r}S_{a-r}}
 \tag{7}
\]
has positive coefficients. It implies
\[
 |e_a(-2\cos u)|\le e_a(-2)
 \quad(u\in\mathbb R,\ 2a<N).
 \tag{8}
\]
Equations (6) and (8), applied term by term in (4), give
\[
 |Z^{\mathcal A}_{S,N}(\mathbf u)|
       \le Z^{\mathcal A}_{S,N}(\mathbf0)
       \qquad(\mathbf u\in\mathbb R^{\partial S}).
 \tag{9}
\]
The right side is nonnegative. This reduction is valid for any
all-low subset \(\mathcal A_N\), including discarded assignments.

## 3. Every Fourier charge in the iterated trace

Let \(f(\mathbf t)\) be a finite Laurent polynomial in
\((e^{it_v})_{v\in S}\), separately even in the variables, and write
\[
 f(\mathbf t)=\sum_{\mathbf r\in\mathbb Z^S}
                  a_{\mathbf r}e^{i\mathbf r\cdot\mathbf t}.
 \tag{10}
\]
Its coefficients are separately symmetric:
\(a_{(r_1,\ldots,r_v,\ldots)}
 =a_{(r_1,\ldots,-r_v,\ldots)}\).
No positivity is needed for the next identity.

Put \(\eta=(-1)^{N-1}\), and extend the coefficients in (10)
by zero outside their finite support. Then
\[
 \begin{split}
 \left(\prod_{v\in S}\phi_N^{(v)}\right)f
 ={}&N^{2k}
 \sum_{\boldsymbol\ell\in\mathbb Z_{>0}^S}
       \left(\prod_{v\in S}\ell_v\eta^{\ell_v+1}\right)\\
 &\qquad{}\times
 \sum_{\boldsymbol\epsilon\in\{-1,1\}^S}
       \left(\prod_{v\in S}(-\epsilon_v)\right)
       a_{N\boldsymbol\ell+\boldsymbol\epsilon}.
 \end{split}
 \tag{11}
\]
The sum is finite because of the coefficient support.

To prove this, use the exact one-variable derivative sampling formula
\[
 \phi_N(f^\sharp)
 =\eta\sum_{j=0}^{N-1}
       (\sin t\,f(t))'\big|_{t=\pi(N-1-2j)/N},
 \qquad f(t)=f^\sharp(-2\cos t).
 \tag{12}
\]
The coefficient of \(e^{irt}\) in the derivative is
\(r(a_{r-1}-a_{r+1})/2\).
Sampling selects \(r=\ell N\), with grid sum \(N\eta^\ell\).
The zero frequency vanishes. The two terms with frequencies
\(\ell N,-\ell N\) are equal by evenness, so their sum is
\[
 N^2\ell\eta^{\ell+1}
       (a_{\ell N-1}-a_{\ell N+1}),\qquad \ell\ge1.
 \tag{13}
\]
Apply (13) successively in every variable. Traces in different
variables commute, proving (11).

Formula (11) includes the original derivatives at repeated roots.
For a fixed all-low wire assignment, the degree in \(t_v\) is
\(L_v=\sum_{e\ni v}a_e\). Charges above
\(\lfloor(L_v+1)/N\rfloor\) do not occur. A trivalent vertex has
only charge one, as in the degree-three proof; higher valence can
produce charges two and above. At even levels their coefficient
signs \(\eta^{\ell_v+1}\) alternate, so they cannot simply be
replaced by the charge-one formula.

For example, at \(N=3\) take \(f=e_1^5\). Its Laurent
polynomial is \((1+w+w^{-1})^5/3^5\). Formula (13) gives
charge-one contribution \(25/27\) and charge-two contribution
\(2/27\), for a total of one. Direct multiplication in the
quotient gives the same result: \(e_1^2=e_1+e_2\) and
\(e_1e_2=0\), so \(\phi_3(e_1^5)=1\).
At \(N=4\), the polynomial
\(e_1^7=(\sqrt2+w+w^{-1})^7/2^7\) has contributions
\(161/4\) and \(-1/4\), totaling \(40\).
This also follows by reducing \((\sqrt2-z)^7/2^7\)
modulo \((z^2-2)^2\) and applying
\(\phi_4(f)=-16[z^3]\operatorname{rem}f\).
These two exact examples show the additional charges and their
parity-dependent signs.

**Positive coefficient bound.** Suppose additionally
\(a_{\mathbf r}\ge0\), and choose any fixed vector
\(\mathbf h=(h_v)_{v\in S}\) with \(h_v>0\).
Then
\[
 \left|\left(\prod_{v\in S}\phi_N^{(v)}\right)f\right|
 \le N^{2k} f(-i\mathbf h)
       \prod_{v\in S}
       \frac{2\cosh h_v\,e^{-Nh_v}}
            {(1-e^{-Nh_v})^2}.
 \tag{14}
\]
Indeed every coefficient in (10) satisfies
\(a_{\mathbf r}\le e^{-\mathbf r\cdot\mathbf h}
 f(-i\mathbf h)\). Insert this inequality in the absolute value
of (11). The sums over \(\epsilon_v\) give \(2\cosh h_v\),
and
\(\sum_{\ell\ge1}\ell e^{-\ell Nh_v}
 =e^{-Nh_v}/(1-e^{-Nh_v})^2\).
The upper bound remains valid when the finite sums are extended
to these convergent infinite sums.

In particular, all higher charges in this bound have a strict
penalty. After selecting a non-unit charge in at least one
coordinate their geometric series has an additional factor
\(O(e^{-N\min_vh_v})\). This controls those charges for the
positive coefficient estimate; it does not supply a nonzero
charge-one contribution.

## 4. A uniform all-low bound and its discarded-index gap

For each assignment in \(\mathcal A_N\), replace the real boundary
angles by zero before forming its Laurent polynomial in the selected
angles. Sum those polynomials and call the result
\(F^{\mathcal A}_N(\mathbf t)\). By (7), its Laurent
coefficients are nonnegative, it is separately even, and its
iterated trace is \(Z^{\mathcal A}_{S,N}(\mathbf0)\).
Equations (9) and (14) give the exact upper bound
\[
 |Z^{\mathcal A}_{S,N}(\mathbf u)|
 \le N^{2k} F^{\mathcal A}_N(-i\mathbf h)
       \prod_{v\in S}
       \frac{2\cosh h_v\,e^{-Nh_v}}
            {(1-e^{-Nh_v})^2}
 \qquad(\mathbf u\text{ real}).
 \tag{15}
\]

To express its exponential rate, put
\[
 J(x)=\int_0^x\log(2\sin\pi s)\,ds,
 \qquad
 b(x,-ih)=
 \int_0^x\log(2\cos(2\pi s)+2\cosh h)\,ds-2J(x)
 \tag{16}
\]
for \(0\le x\le1/2\), using the continuous endpoint values.
When \(h=0\), the final numerator has an integrable logarithmic
zero at \(x=1/2\). For a boundary vertex outside \(S\), set
its height equal to zero.
For an edge \(e=vw\in E_S\), define
\[
 A_e(x;\mathbf h)=b(x,-ih_v)+b(x,-ih_w).
 \tag{17}
\]
Uniform comparison of the sine factorials and cosine products
with their integrals yields
\[
 \log\{e_a(-2\cosh h_v)e_a(-2\cosh h_w)\}
     =N A_e(a/N;\mathbf h)+O_{\mathbf h}(\log N)
 \tag{18}
\]
for all low indices, including both endpoints of their range.
The endpoint argument is written in
[the degree-three tail proof, Section 3](research_degree_three_zero_wire_tails.md#3-uniform-elementary-estimates-at-every-boundary-of-the-index-range).
There are only polynomially many assignments for the fixed graph.
Therefore (15) gives
\[
 |Z^{\mathcal A}_{S,N}(\mathbf u)|
 \le C N^A
 \exp N\left\{
   \sup_{\mathbf x\in\overline{\mathcal A}}
       \sum_{e\in E_S}A_e(x_e;\mathbf h)
           -\sum_{v\in S}h_v\right\}.
 \tag{19}
\]
Here \(\overline{\mathcal A}\subset[0,1/2]^{E_S}\) can be
any fixed closed set containing all the normalized index assignments
under consideration. The constants can absorb the fixed product
in (15) after its leading \(e^{-N\sum h_v}\) is extracted.

There is a particularly useful regime. Suppose
\[
 \sinh(h_v/2)\sinh(h_w/2)<1
            \qquad(vw\text{ internal}).
 \tag{20}
\]
The analogous inequality is automatic on a boundary edge because
the outside height is zero. For \(0<x<1/2\), each \(A_e\)
is strictly concave:
\[
 A_e''(x)=\sum_{r\in\{v,w\}}
 \left\{-\frac{2\pi\sin(2\pi x)}
                {\cos(2\pi x)+\cosh h_r}
       -2\pi\cot(\pi x)\right\}<0.
 \tag{21}
\]
Its derivative tends to positive infinity at zero. When both
heights are positive, its derivative at \(1/2\) is
\[
 A_e'(1/2)=
    2\log\{\sinh(h_v/2)\sinh(h_w/2)\}<0.
 \tag{22}
\]
If one height is zero the derivative tends to negative infinity.
Thus each edge has a unique maximum \(x_e(\mathbf h)\)
strictly inside \((0,1/2)\), determined by
\[
 \cos(2\pi x_e)=
 \frac{1-\cosh h_v\cosh h_w}
      {2+\cosh h_v+\cosh h_w}.
 \tag{23}
\]
Let \(\psi(-ih_v,-ih_w)\) denote this maximum value. These
positive real critical values continue the original edge phase
along the segment of heights from zero to \(\mathbf h\);
(20) remains strict on that segment. Set
\[
 \mathcal M(\mathbf h)=
 \sum_{e=vw\in E_S}\psi(-ih_v,-ih_w)
                          -\sum_{v\in S}h_v.
 \tag{24}
\]

Choose, for every edge, a closed interval
\(I_e\subset(0,1/2)\) containing \(x_e(\mathbf h)\)
in its interior. Strict concavity and compactness give a number
\(\delta>0\) such that the supremum in (19), when at least one
\(x_e\notin I_e\), is at most
\(\mathcal M(\mathbf h)-\delta\) after subtracting \(\sum h_v\).
Consequently
\[
 \sup_{\mathbf u\text{ real}}
 |\text{all-low terms with some }a_e/N\notin I_e|
 \le C N^A e^{N(\mathcal M(\mathbf h)-\delta)}.
 \tag{25}
\]
This proves a uniform discarded-index estimate for the whole all-low
part. It requires neither a small-height assumption nor an a priori
action gap relative to the complete tree. Its strictness comes from
the individual real wire maxima after the Fourier trace bound.
The source is separately of degree at most \(N-1\) in each boundary
spectral variable, so the gap persists on a sufficiently small
complex polydisk by the usual Chebyshev coefficient estimate.

No stationary equation in the selected angles was used for
(19) or (25). To turn \(\mathcal M(\mathbf h)\) into a
stationary-phase action, one still has to choose \(\mathbf h\)
so that all selected derivatives vanish and to prove the nonzero
asymptotic for the retained contribution.

## 5. An explicit obstruction to an arbitrary regular saddle

In the regular region (20), the selected charge-one stationary
equations are
\[
 \sum_{w\sim v}
 \arcsin\{\tanh(h_v/2)\cosh(h_w/2)\}=\pi
                         \qquad(v\in S).
 \tag{26}
\]
The outside heights are again zero. Each inverse sine in (26)
is the real value in \((0,\pi/2)\), because (20) is equivalent
to its argument being less than one. Equation (26) follows by
substituting \(t_v=-ih_v\) into
\[
 \psi_t(t,u)=-\pi^{-1}\operatorname{arsinh}
                          (\tan(t/2)\cos(u/2))
 \tag{27}
\]
and imposing \(\sum_{w\sim v}\psi_t(t_v,t_w)=i\).

Consider the selected set consisting of two adjacent vertices,
both of original degree three. Each has two free neighbors.
Put \(a=\sinh(h_1/2)\), \(b=\sinh(h_2/2)\). Regularity
requires \(ab<1\). The two equations (26) become
\[
 \arcsin\frac{a\sqrt{1+b^2}}{\sqrt{1+a^2}}
       +2\arctan a=\pi,\qquad
 \arcsin\frac{b\sqrt{1+a^2}}{\sqrt{1+b^2}}
       +2\arctan b=\pi.
 \tag{28}
\]
Both inverse sines are strictly less than \(\pi/2\).
The first equation therefore requires \(a>1\), and the second
requires \(b>1\), contradicting \(ab<1\).

There is thus no regular interior imaginary saddle for this
selected subtree. At the symmetric limiting point \(a=b=1\),
the internal edge in (23) has \(x_e=1/2\), so precisely an
endpoint of the low wire range is reached.
This does not prove that the partially filled manifold is
nonhyperbolic, or that its full polynomial has no useful asymptotic.
It rules out a universal proof which assumes the regular saddle
and the interior wire maxima used in (25).

## 6. What the high indices still require

The matching restriction in Section 2 is exact, but it is not
an exponential estimate. A high internal edge affects the two
selected traces at its endpoints. It cannot be estimated as a
high boundary index at a single isolated vertex.

One coefficient inequality remains available at every nonnegative
imaginary height. Suppose exactly one
incident index at a vertex is high, with value \(i\), and let
\[
 \prod_{j=1}^{d-1}e_{a_j}
     \equiv\sum_{r=0}^{N-1}c_r e_r\pmod{P_N},
 \qquad c_r\ge0,
 \tag{29}
\]
where the other indices \(a_j\) are low. Then the actual trace
is \(c_{N-1-i}\). Moreover, for every \(h\ge0\),
\[
 c_r e_r(-2\cosh h)
       \le\prod_{j=1}^{d-1}e_{a_j}(-2\cosh h)
                 \qquad(0\le r<N).
 \tag{30}
\]
To prove (30), multiply successively using (5).
When the index sum is below \(N\), its polynomial identity
preserves evaluation at \(z_h=-2\cosh h\). When it is at least
\(N\), quotient multiplication drops that term. Every Newton
factor \(c_j-z_h\) is nonnegative, so the unreduced evaluation
of the dropped term is nonnegative. More explicitly, if the positive
representative after several factors is \(R=\sum c_r e_r\), then
reducing \(Re_a\) by (5) can only decrease its value at \(z_h\).
Multiplication by the nonnegative \(e_a(z_h)\) preserves the
preceding induction inequality. Thus the evaluation of the nonnegative
quotient representative can only decrease relative to the
unreduced product. Selecting its \(r\)-th nonnegative term gives
(30). For \(r=N-1-i\), this is a low index and
\(e_r(z_h)>0\), including at \(h=0\), so division is
legitimate:
\[
 \phi_N\left(e_i\prod_{j=1}^{d-1}e_{a_j}\right)
 \le
 \frac{\prod_{j=1}^{d-1}e_{a_j}(-2\cosh h)}
      {e_{N-1-i}(-2\cosh h)}.
 \tag{31}
\]

## 7. A constrained profile for each matching of high edges

Fix a nonempty set \(H\subset E_S\) of high edges, subject to the
matching condition at every selected vertex. Let \(V_H\subset S\)
be their selected endpoints. At a vertex \(v\in V_H\), denote
its unique incident high edge by \(e_H(v)\). Every other selected
vertex has only low incident indices.

Put \(D=N-1\). For this section normalize indices by \(D\):
\[
 x_e=\frac{a_e}{D}\quad(e\notin H),\qquad
 y_e=\frac{D-i_e}{D}\quad(e\in H).
 \tag{32}
\]
Here \(a_e\) is a low index and \(i_e\) is a high index. Both
\(x_e\) and \(y_e\) belong to \([0,1/2]\). Define the fixed
closed polytope \(\mathcal P_H\) by those box constraints and
\[
 \begin{aligned}
 \sum_{e\ni v}x_e&\ge1
                         &&(v\in S\setminus V_H),\\
 \max_{\substack{e\ni v\\e\notin H}}x_e
    \ \le\ y_{e_H(v)}
    &\le \sum_{\substack{e\ni v\\e\notin H}}x_e
                         &&(v\in V_H).
 \end{aligned}
 \tag{33}
\]
When the second line has no low factors, take its maximum and sum
to be zero.
Every nonzero finite assignment with high-edge set \(H\)
satisfies (33). At an unmatched vertex, a product of total degree
less than \(D\) has zero trace, proving the first condition.
At a matched vertex, every intermediate output in the positive
product (5) is at least each input and at most their sum.
Hence the coefficient \(c_{D-i}\) can be nonzero only if
\(\max a_j\le D-i\le\sum a_j\), which is the second condition.
Only this necessary support property is used below.

Choose arbitrary fixed heights \(h_v>0\) for \(v\in S\);
outside heights are zero. These heights need not satisfy (20).
Define on \(\mathcal P_H\)
\[
 \begin{split}
 \mathcal B_H(\mathbf x,\mathbf y;\mathbf h)
 ={}&
 \sum_{\substack{e=vw\in E_S\\e\notin H}}
       \{b(x_e,-ih_v)+b(x_e,-ih_w)\}\\
 &-\sum_{v\in S\setminus V_H}h_v
   -\sum_{v\in V_H}b(y_{e_H(v)},-ih_v).
 \end{split}
 \tag{34}
\]
In particular an internal high edge contributes a complementary
Newton denominator at each of its two selected endpoints. A high
boundary edge contributes one such denominator. Matched vertices
do not also receive a charge penalty \(-h_v\): their trace has
been bounded by the coefficient extraction (31).

**Matching bound.** Let \(Z^H_{S,N}\) be the part of the original
source with precisely the high-edge set \(H\). There are constants
\(C,A\), depending on the fixed tree and heights, such that
\[
 \sup_{\mathbf u\text{ real}}|Z^H_{S,N}(\mathbf u)|
 \le C N^A
  \exp\left\{N\max_{(\mathbf x,\mathbf y)\in\mathcal P_H}
                  \mathcal B_H(\mathbf x,\mathbf y;\mathbf h)\right\}.
 \tag{35}
\]
An empty polytope means that this part of the source vanishes.

To prove (35), fix one assignment. At every matched vertex use
(31). At every unmatched vertex apply the one-variable case of
(14) to the product of its low incident Newton factors. Its
Laurent coefficients are nonnegative, so this incurs the factor
\[
 N^2\,\frac{2\cosh h_v\,e^{-Nh_v}}
                 {(1-e^{-Nh_v})^2}
 \tag{36}
\]
and evaluates all those factors at \(-2\cosh h_v\).
For a low boundary edge use (8) at the outside endpoint.
For a high boundary edge use the uniform polynomial interval bound
for \(e_{i_e}\), which includes the first derivatives at double
roots; see
[the degree-three tail proof, Section 3](research_degree_three_zero_wire_tails.md#3-uniform-elementary-estimates-at-every-boundary-of-the-index-range).
Multiplying these estimates gives exactly the positive factors and
reciprocal factors displayed in (34), with the exponential penalty
in (36) only at unmatched vertices.

The uniform factorial estimates used in (18) apply also to the
low complementary indices in the denominators. Their two-sided
logarithmic error is \(O(\log N)\), including the endpoints.
Replacing the usual normalized argument \(a/N\) by \(a/D\)
in the continuous functions changes the resulting logarithm by
only \(O(\log N)\). One way to see this uniformly is to separate
the endpoint terms \(x\log x\) and
\((1/2-x)\log(1/2-x)\) from \(b\): each has modulus of
continuity \(O(\varepsilon|\log\varepsilon|)\), and
\(|a/N-a/D|\le1/(2N)\). The remaining terms have bounded
derivative on the closed interval. The same argument applies to
\((D-i)/N\). Consequently each assignment has the upper rate
\(\mathcal B_H\), with a uniform polynomial prefactor.
All nonzero assignments lie in \(\mathcal P_H\), and their
number is polynomial in \(N\). This proves (35).

Since (35) holds for every fixed positive height vector, it also
gives the optimized upper bound
\[
 \limsup_{N\to\infty}\frac1N
       \log\sup_{\mathbf u\text{ real}}|Z^H_{S,N}(\mathbf u)|
 \le
 \inf_{\mathbf h\in(0,\infty)^S}
       \max_{\mathcal P_H}\mathcal B_H(\mathbf x,\mathbf y;\mathbf h).
 \tag{37}
\]
There are finitely many matchings \(H\) in the fixed tree, so
their finite sum is controlled by the largest of these bounds.
No exchange of an infimum with a maximum has been made.

To see exactly what a comparison with the all-low bound requires,
put
\[
 V_e(\mathbf h)=\max_{0\le x\le1/2}A_e(x;\mathbf h),
 \qquad
 \mathcal L(\mathbf h)=\sum_{e\in E_S}V_e(\mathbf h)
                                      -\sum_{v\in S}h_v.
\]
Direct subtraction of (34) gives
\[
 \begin{split}
 \mathcal L(\mathbf h)-\mathcal B_H
 ={}&\sum_{e\notin H}\{V_e-A_e(x_e;\mathbf h)\}\\
 &+\sum_{\substack{e=vw\in H\\v,w\in S}}
       \{V_e+A_e(y_e;\mathbf h)-h_v-h_w\}\\
 &+\sum_{\substack{e=vw\in H\\v\in S,\ w\notin S}}
       \{V_e+b(y_e,-ih_v)-h_v\}.
 \end{split}
 \tag{38}
\]
The low-edge terms in the first line are nonnegative. The other
terms are not known to be nonnegative separately; the constraints
(33) connect them to the low-edge losses. Thus a proof of a strict
global gap must use those constraints or a sharper coefficient
estimate, rather than simply compare an isolated high-edge term
with its unconditioned maximum.

This is an explicit optimization problem for all the high-index
terms. It does not prove that its value is below the selected
all-low rate. That comparison remains necessary even when a
regular coupled stationary point exists. The degree-three isolated
vertex used an additional exact compact profile argument; it did
not follow from a matching restriction alone.

The results of this note therefore isolate three separate questions
for a connected all-zero subtree: find the appropriate selected
stationary configuration, estimate the matching of high edges, and
compute a nonzero leading contribution. The exact Fourier identity
(11), the all-charge upper bound (15), and the all-low discarded
gap (25) supply part of the analytic argument. They do not settle
the other questions or imply finite exceptions for arbitrary templates.
