# The discarded terms at a degree-three vertex with zero crossing power

Research proof, 2 November 2026. This note supplies the omitted-index
estimate missing from the degree-three case of
[the zero-power boundary theorem](research_zero_power_internal_boundary_theorem.md).
It uses the exact multiplication and closing functional in the original
Newton basis. The proof below is separate from the local stationary-phase
argument and from the geometric interpretation of its action.

## 1. The polynomial and the estimate to prove

Fix an integer level \(N\ge3\), and put \(D=N-1\). Write
\[
 S_k=\prod_{r=1}^k2\sin(\pi r/N),\qquad S_0=1,\qquad
 c_j=2\cos((2j+1)\pi/N),
\]
\[
 e_k(z)=S_k^{-2}\prod_{j=0}^{k-1}(c_j-z),\qquad 0\le k<N.
 \tag{1}
\]
The full pair algebra is the polynomial quotient by
\[
 P_N(z)=\prod_{j=0}^{N-1}(z-c_j).
 \tag{2}
\]
Its double roots retain their first derivatives. The closing
functional is
\[
 \phi_N(f)=(-1)^D N^2[z^D]\operatorname{rem}_{P_N}f.
 \tag{3}
\]
In particular, it is not evaluation at the distinct roots.
For real boundary angles \(\mathbf u=(u_1,u_2,u_3)\), the original
degree-three zero-power polynomial is
\[
 P_{3,0,N}(\mathbf u)=
 \sum_{i,j,k=0}^{N-1}
 \phi_N(e_i e_j e_k)
 e_i(-2\cos u_1)e_j(-2\cos u_2)e_k(-2\cos u_3).
 \tag{4}
\]
Every boundary remains open in (4).

Call an index low when \(2k<N\), and high otherwise.
Define the continuous real functions
\[
 J(x)=\int_0^x\log(2\sin\pi v)\,dv,\quad 0\le x\le1,
 \qquad
 g(x)=J(2x)-4J(x),\quad 0\le x\le\tfrac12.
 \tag{5}
\]
Let \(G\) be Catalan's constant and set \(M_\infty=4G/\pi\).
The elementary identities
\[
 g(0)=g(1/2)=0,\qquad
 g'(x)=2\log\cot(\pi x),\qquad
 g''(x)=-\frac{4\pi}{\sin(2\pi x)}
 \tag{6}
\]
show that \(g\ge0\), with its unique maximum
\[
 g(1/4)=\frac{M_\infty}{2}.
 \tag{7}
\]
Put
\[
 h=2\operatorname{arsinh}\sqrt3,\qquad
 x_*=\frac{\arctan2}{\pi}.
 \tag{8}
\]
The selected action at the degree-three zero-power vertex is
\[
 M_3=3\psi(-ih,0)-h=2M_\infty.
 \tag{9}
\]
The exact equality in (9) is proved by the Fourier integral calculation
in [the action-gap lemma, Section 3](research_isolated_vertex_action_gap.md#3-the-exact-endpoint-value-at-degree-three).
Here \(\psi\) is the critical value of the edge phase defined in
Section 5 below.

**Proposition.** Fix any closed interval
\(I=[\alpha,\beta]\subset(0,1/2)\) with \(x_*\) in its
interior. Let \(P^I_{3,0,N}\) denote (4) with all three normalized
indices in \(I\). There are constants \(C,A,\delta>0\), depending
on \(I\), such that
\[
 \sup_{\mathbf u\in\mathbb R^3}
 \left|P_{3,0,N}(\mathbf u)-P^I_{3,0,N}(\mathbf u)\right|
 \le C N^A e^{N(M_3-\delta)}.
 \tag{10}
\]
The bound holds at both even and odd levels. The omitted polynomial
also has a strict exponential gap on a sufficiently small fixed
complex polydisk about \(\mathbf u=0\).

The coarse estimate \((d-1)M_\infty\) for a high index equals \(M_3\)
when \(d=3\), so it cannot prove (10). The proof has two parts.
The exact positive product bounds the terms with one high index.
A Fourier coefficient inequality bounds the all-low terms.

## 2. Exact positivity, including the double-root derivatives

The [Newton multiplication calculation](../papers/newton-calculus/finite.tex)
gives the polynomial identity
\[
 e_i e_j=\sum_{r=\max(i,j)}^{i+j}\mu_{ijr}e_r,\qquad
 \mu_{ijr}=
 \frac{S_{i+j}S_r}
 {S_iS_jS_{r-i}S_{r-j}S_{i+j-r}}>0
 \quad(i+j<N).
 \tag{11}
\]
This is an identity of polynomials of degree less than \(N\).
For completeness, it follows by multiplying the unnormalized Newton
polynomials successively by \(c_i-z\), using
\[
 (c_i-z)B_r=B_{r+1}+(c_i-c_r)B_r,\qquad
 B_r=\prod_{j<r}(c_j-z).
 \tag{12}
\]
At a generic parameter the required two-term coefficient identity is
\([i+1][i+j+1]=[r][r-j]+[r+i+1][i+j+1-r]\).
Expanding the four powers in each quantum integer proves it; regular
specialization then gives (11), whose factorial indices are all below
\(N\).

When \(i+j\ge N\), the product is zero in the full quotient (2).
Indeed \(c_{D-a}=c_a\), so
\[
 B_N/B_j=B_{N-j}.
 \tag{13}
\]
Since \(i\ge N-j\), \(B_iB_j\) is divisible by \(B_N=(-1)^N P_N\).
This divisibility includes the multiplicity of every root, so it
annihilates the first normal derivatives as well as the values.

Equation (3) gives
\[
 \phi_N(e_r e_k)=\mathbf1_{r+k=D}.
 \tag{14}
\]
For \(r+k<D\) this is a degree statement. For \(r+k=D\), the
leading coefficient and \(S_rS_{D-r}=N\) give the value one.
For \(r+k>D\), (13) gives zero. Thus (14) is a statement about the
full closing functional, with no replacement by a simpler nodal trace.

Combining (11) and (14) proves
\[
 \phi_N(e_i e_j e_k)=\mu_{ij,D-k}
 \tag{15}
\]
on the support
\[
 i+j\le D,\quad i+k\le D,\quad j+k\le D,\quad i+j+k\ge D;
 \tag{16}
\]
outside it the coefficient is zero. Every coefficient in (4) is
therefore nonnegative. Two high indices have sum at least \(N\),
so all terms with at least two high indices vanish exactly.
Neither assertion loses the double-root derivatives.

## 3. Uniform elementary estimates at every boundary of the index range

We record the estimates used in both parts of the proof:
\[
 \log S_r=NJ(r/N)+O(\log N),\qquad 0\le r<N,
 \tag{17}
\]
\[
 \log e_k(-2)=Ng(k/N)+O(\log N),\qquad 2k<N.
 \tag{18}
\]
The constants are uniform in the indices. To see (17), split
\(\log(2\sin\pi x)\) into its endpoint logarithms
\(\log x+\log(1-x)\) and a smooth function on \([0,1]\).
Comparison of the logarithmic sums with their integrals, or the
elementary factorial bounds for those two sums, has error
\(O(\log N)\), including \(r=0,N-1\). The smooth part has bounded
sum--integral error. For (18) use
\[
 e_k(-2)=S_k^{-2}\prod_{j<k}4\cos^2((j+1/2)\pi/N).
 \tag{19}
\]
The midpoint logarithm has a single endpoint singularity at \(1/2\).
Its closest included midpoint is at distance at least \(1/(2N)\)
from that endpoint. Separating the last mesh interval and integrating
the logarithm gives a uniform \(O(\log N)\) error. The integral of
the logarithm in the numerator is \(J(2x)-2J(x)\), proving (18).
Thus neither formula requires the normalized index to remain in
an interior compact interval.

For a low index, the exact positive Laurent formula is
\[
 e_k(-2\cos t)=\frac{S_{2k}}{S_k^2}
       \sum_{r=-k}^k\frac{e^{irt}}{S_{k+r}S_{k-r}},
 \qquad 2k<N.
 \tag{20}
\]
The finite Gaussian-binomial identity proves (20), as detailed in
[the zero-power note, Section 2](research_zero_power_internal_boundary_theorem.md#2-positive-laurent-coefficients-and-angular-decrease).
All factorial indices in (20) are below \(N\). In particular,
\[
 |e_k(-2\cos u)|\le e_k(-2)\qquad(u\in\mathbb R,\ 2k<N).
 \tag{21}
\]

For high indices there are uniform constants \(C,A_0\) such that
\[
 \sup_{u\in\mathbb R}|e_k(-2\cos u)|\le C N^{A_0}.
 \tag{22}
\]
We recall why this is a polynomial bound for the full polynomial,
not just a bound at the distinct nodes. Put \(l=N-k\).
The polynomial vanishes at all the distinct roots of \(P_N\).
At a double root \(c_j\), its derivative is zero unless \(j<l\),
and otherwise
\[
 |e_k'(c_j)|=
 \frac{S_{l-1}^{\,2}}
 {2\sin((2j+1)\pi/N)S_{l+j}S_{l-1-j}}
 \le \frac{N^2}{16}.
 \tag{23}
\]
The factorial ratio in its denominator starts at \(2\sin(l\pi/N)\)
and increases with \(j\): the successive ratio is
\(\sin((l+j+1)\pi/N)/\sin((l-1-j)\pi/N)\ge1\).
This proves (23) using the sine chord bound.
Hermite interpolation at the complete Chebyshev nodes has polynomial
conditioning. One explicit proof first interpolates values at the
distinct roots by their Chebyshev node polynomial, subtracts that
interpolant, divides by the node polynomial, and interpolates the
remaining derivatives. The distinct-node polynomial and its derivatives
have polynomial interval norm, while its derivatives at its roots are
bounded below by \(N/2\). At odd levels the simple root \(-2\)
is omitted from the second interpolation: divide the node polynomial
by \(z+2\), which lowers the derivative bound at a remaining root
by at most the factor four. These formulas give (22).
The full details and (23) are in
[the finite Hermite bound](../papers/circle-tree-volume/finite-bounds.tex).

## 4. A strict gap for every term with one high index

Suppose \(i\) is high. Terms with \(j\) or \(k\) high have already
vanished. Put
\[
 a=\frac{D-i}{N},\qquad y=\frac jN,\qquad z=\frac kN.
 \tag{24}
\]
Then \(j,k,D-i\) are low, and (15), applied with the product
\(e_j e_k\), gives the coefficient \(\mu_{jk,D-i}\).
Its support lies in the compact polytope
\[
 \mathcal Q=\{(y,z,a):0\le y,z\le a\le\tfrac12,\ a\le y+z\}.
 \tag{25}
\]
Define on this whole polytope
\[
 m(y,z,a)=J(y+z)+J(a)-J(y)-J(z)
          -J(a-y)-J(a-z)-J(y+z-a).
 \tag{26}
\]
Every argument of \(J\) belongs to \([0,1]\), so \(m\) is
continuous on all boundary faces. Equations (17), (18), and (22)
bound each term of (4), uniformly over all real parents, by
\[
 CN^A\exp N F(y,z,a),\qquad
 F(y,z,a)=m(y,z,a)+g(y)+g(z).
 \tag{27}
\]
There is no unrecorded shift of a factorial argument in (26):
\(a\) was defined using the exact integer \(D-i\).

We need a stronger bound than the separate maximum of each factor.
Evaluate the exact polynomial identity (11) at \(-2\).
All terms in that identity are nonnegative, since
each \(e_r(-2)\) is a product of nonnegative factors. Consequently
\[
 \mu_{jkr}e_r(-2)\le e_j(-2)e_k(-2)
 \quad\text{whenever } j,k,r\text{ are low and }
 \max(j,k)\le r\le j+k.
 \tag{28}
\]
Taking logarithms, dividing by \(N\), and using the uniform errors
in (17)--(18) gives the continuous inequality
\[
 m(y,z,a)+g(a)\le g(y)+g(z)
 \qquad((y,z,a)\in\mathcal Q).
 \tag{29}
\]
Here is a justification including the faces \(a=1/2\) and \(y+z=1\).
The relative interior points with \(a<1/2\) are approximated by
integer triples satisfying the same strict inequalities. For those
triples (28) has strictly positive factors and no factorial index
equal to \(N\). Passing to the limit proves (29) there. Such
interior points are dense in \(\mathcal Q\), and continuity of
\(J\) proves (29) on its remaining faces.

Since \(g(a)\ge0\), equations (7) and (29) imply
\[
 F(y,z,a)\le2g(y)+2g(z)-g(a)\le2M_\infty.
 \tag{30}
\]
Equality in (30) would require \(y=z=1/4\) and \(g(a)=0\).
The support then forces \(a=1/2\). At that one possible point,
however,
\[
 m(1/4,1/4,1/2)=g(1/4)=M_\infty/2,\qquad
 F(1/4,1/4,1/2)=3M_\infty/2<2M_\infty.
 \tag{31}
\]
Thus equality is impossible. Compactness now gives
\[
 \delta_{\rm high}:=2M_\infty-\max_{\mathcal Q}F>0.
 \tag{32}
\]
This is an existence proof of a fixed positive gap; it does not
depend on a numerical maximization. At most \(3N^3\) terms have
one specified high index. Equations (27) and (32) bound their
total by a polynomial times \(e^{N(M_3-\delta_{\rm high})}\).

## 5. A Fourier bound for the all-low terms

Fix a low triple \((i,j,k)\), and write
\[
 f(t)=e_i(-2\cos t)e_j(-2\cos t)e_k(-2\cos t)
     =\sum_{m=-L}^L a_m e^{imt},\qquad L=i+j+k.
 \tag{33}
\]
Equation (20) gives \(a_m\ge0\) and \(a_{-m}=a_m\).
Also \(L\le3\lfloor(N-1)/2\rfloor\), so \(L+1<2N\).
Extend \(a_m\) by zero outside \([-L,L]\).

The [exact derivative sampling formula](research_exact_complete_trace_contour.md#1-the-original-finite-trace-at-the-complete-meridian)
is
\[
 \phi_N(f^\sharp)=\eta\sum_{j=0}^{N-1}
       (\sin t\,f(t))'\big|_{t=\tau_j},\qquad
 \eta=(-1)^{N-1},\quad
 \tau_j=\frac{\pi(N-1-2j)}N,
 \tag{34}
\]
where \(f(t)=f^\sharp(-2\cos t)\).
This formula agrees with (3), including the first derivatives at
the double roots. Indeed the two grid points \(\tau,-\tau\)
above a double root \(c=-2\cos\tau\) contribute
\((4-c^2)(f^\sharp)'(c)-cf^\sharp(c)\) before the factor
\(\eta\). At an odd level the single point \(\tau=0\)
contributes \(f^\sharp(-2)\). These are exactly the Hermite
terms of the closing functional (3).
The coefficient of \(e^{imt}\) in the derivative in (34) is
\[
 \frac m2(a_{m-1}-a_{m+1}).
 \tag{35}
\]
The grid sum of \(e^{im\tau_j}\) is zero unless \(m=\ell N\),
when it is \(N\eta^\ell\). The frequency zero contributes zero
in (35), and \(L+1<2N\) leaves only \(m=N,-N\).
The outer sign \(\eta\) cancels their grid sign \(\eta\).
Their two equal contributions therefore give the exact identity
\[
 \boxed{\displaystyle
 \phi_N(e_i e_j e_k)=N^2(a_{N-1}-a_{N+1}).}
 \tag{36}
\]
This derivation explains both the sign and the factor \(N^2\);
neither depends on the parity of \(N\).
Positivity from Section 2 gives
\[
 0\le\phi_N(e_i e_j e_k)
 \le N^2a_{N-1}
 \le N^2e^{-(N-1)h}f(-ih).
 \tag{37}
\]
The last inequality follows by selecting the nonnegative term
\(a_{N-1}e^{(N-1)h}\) from \(f(-ih)=\sum a_m e^{mh}\).
The subtraction in (36) has not been replaced by a false positive
trace formula; it supplies the upper bound (37).

Multiplying (37) by the absolute boundary factors and applying
(21) gives, for every real \(\mathbf u\),
\[
 \begin{split}
 &\left|\phi_N(e_i e_j e_k)
       e_i(-2\cos u_1)e_j(-2\cos u_2)e_k(-2\cos u_3)\right|\\
 &\qquad\le N^2e^{-(N-1)h}
       \prod_{\ell\in\{i,j,k\}}
                   e_\ell(-2\cosh h)e_\ell(-2).
 \end{split}
 \tag{38}
\]
Let
\[
 b(x,t)=\int_0^x\log(2\cos(2\pi v)+2\cos t)\,dv-2J(x),
 \qquad A(x)=b(x,-ih)+b(x,0),
 \tag{39}
\]
using real logarithms for \(t=-ih,0\) and \(0\le x<1/2\),
and their continuous limits at \(x=1/2\).
The positive height makes the first numerator logarithm smooth
on the entire interval. Equations (17)--(19) consequently imply
\[
 \log\{e_\ell(-2\cosh h)e_\ell(-2)\}
     =NA(\ell/N)+O(\log N),\qquad 2\ell<N,
 \tag{40}
\]
uniformly including the low endpoint indices.

For \(0<x<1/2\),
\[
 A''(x)=
 \sum_{v\in\{-ih,0\}}\left\{
 -\frac{2\pi\sin(2\pi x)}{\cos(2\pi x)+\cos v}
 -2\pi\cot(\pi x)\right\}<0.
 \tag{41}
\]
Its derivative tends to positive infinity at zero and to negative
infinity at \(1/2\). The stationary equation gives
\[
 \tan(\pi x_*)=\cosh(h/2)=2.
 \tag{42}
\]
Thus \(A\) has the unique maximum
\(A(x_*)=\psi(-ih,0)\). The latter equality is the definition
of the edge critical value, with the positive real logarithms
continued from height zero.

Since \(I\) contains \(x_*\) in its interior, continuity and
strict concavity imply
\[
 \delta_I=A(x_*)-\max_{x\in[0,1/2]\setminus(\alpha,\beta)}
                         A(x)>0.
 \tag{43}
\]
If at least one normalized index of an all-low triple is outside
\(I\), (38)--(43) give the uniform upper rate
\[
 A(i/N)+A(j/N)+A(k/N)-h
       \le3\psi(-ih,0)-h-\delta_I=M_3-\delta_I.
 \tag{44}
\]
The factor \(e^h\) from \(N-1\) in (38), all logarithmic errors
in (40), and the number of triples contribute only a polynomial
prefactor. This proves the required gap for every all-low omitted
term.

## 6. Completion and complex boundary continuation

Every omitted term in (4) belongs to one of the cases just proved:
at least two high indices, whose coefficient vanishes; exactly
one high index, covered by (32); or all indices low with at least
one outside \(I\), covered by (44). The triangle inequality and
polynomially many terms prove (10), with any fixed
\(0<\delta<\min(\delta_{\rm high},\delta_I)\).

The difference in (10) is a polynomial of degree at most \(N-1\)
in each variable \(-2\cos u_j\). A separate Chebyshev expansion
therefore extends its real spectral-cube bound by at most
\[
 C N^3\exp\{N(|\Im u_1|+|\Im u_2|+|\Im u_3|)\}.
 \tag{45}
\]
Indeed the Chebyshev coefficients are bounded by fixed multiples
of the interval supremum, there are at most \(N^3\) of them,
and a term of degree at most \(N-1\) has modulus at most
\(e^{N|\Im u_j|}\) in that variable. Choosing the sum of the
three imaginary radii smaller than \(\delta/2\) preserves a
strict gap. This proves the complex-polydisk assertion.

This proposition supplies the discarded-index estimate used in the
degree-three case of the zero-power theorem. Its retained full-circle
calculation then gives the whole-boundary asymptotic and the leading
value \(A_3(0)=1/16\), as stated in that theorem.
The proposition alone is not an assertion about connected short
filling clusters or about finite exceptions for an arbitrary template.

## 7. Reproducing the finite identities

Run

```sh
python3 experiments/audit_degree_three_zero_trace.py --output repro/results/research-degree-three-zero-trace.json
```

The script computes the closing functional by exact polynomial division
by \(2T_N(z/2)+2\) in a cyclotomic field. It compares that calculation
with the pairing (14), the product coefficient (15), and the Fourier
formula (36), including both level parities and the vanishing terms
with several high indices. Polynomial division retains the repeated
roots and their derivatives. These finite calculations check the
identities and normalization; the uniform exponential gaps are proved
in Sections 4 and 5.
