# Quantum-binomial divisors and generic physical-window rank

Private written proof, 16 November 2026.

For a fixed exact repeated-turn window, generic rank failure on a
rational physical trajectory is equivalent to a common explicit
quantum-binomial divisor of its full-column minors. This is a
criterion for the complete finite-level rows, including normals and
their actual clearings. It does not prove that the common divisor
is absent for every active product.

## 1. Actual rows and bounded coefficient degrees

Fix all powers, arities, and a finite window of translated rows of
the full-step interface. Include the first-normal rows and whichever
original recovery constraints are used. Specify the unknown packet
and the supplied packets as in the pinned conditioning theorem:
\[
                    \mathsf A_N X_N=F_N-\mathsf L_N B_N .
 \tag{1}
\]
Matrix size and shift ranges are independent of \(N\). No additional
future component is silently treated as known. Put
\[
 h=N^{-1},\quad q=e^{\pi ih},\quad v=q^{2j+1},\qquad
 w_i=2\cosh(\alpha_i h),\quad
 p_i=P_N(w_i)=4\cosh^2(\alpha_i/2).
 \tag{2}
\]
In coefficient calculations these are initially independent symbols.
Use one pair \((w_i,p_i)\) per independent microscopic parameter.
Identify literal repeated parameters before forming minors.
Alternatively use the polarized independent family and later
specialize its actual source. Generic rank in that ambient family
is not asserted to hold on every shared-parameter diagonal.

After the specified polynomial clearings and removal of harmless
scalar denominators, the exact window matrix is represented over
\[
 \mathscr R=\mathbb C[h,h^{-1},q,q^{-1},v,v^{-1},
                              w_1,p_1,\ldots,w_s,p_s].
 \tag{3}
\]
Its degrees are bounded by the fixed window and input data.
A harmless scalar denominator here is nonzero at all sufficiently
large physical levels under consideration; clearing it multiplies
the entire equation, including its source. Physical nonunit factors
are instead retained in the polynomial rows.

Indeed the original matrices use finitely many rational operations
in (2), the fixed-shift \(A,B\) coefficients, and the displayed
ordinary product-module coefficients. The varying-level polynomial
\(P_N\) stays in a source channel, or is evaluated at an endpoint
as the symbol \(p_i\). A full step replaces \(v\) by \(q^{2k}v\);
a coefficient normal is \(2\pi i v\partial_v\). Neither changes
bounded-degree rationality. Fixed matrix products and clearings,
and forming a finite row window, preserve this property.
A canonical source polynomial of degree depending on \(N\), or a
terminal function \(G_n\), is not promoted to a coefficient in (3).

Known columns may be removed exactly first. After the ordinary
half-step aliases have been completed and the full step formed,
a canonical \(P_N\) channel is zero with all physical first angular
normals. A constant with a fixed-degree polynomial gauge is known.
Under \(V_n\) it remains fixed-degree: \(T\) maps the degree flag to
a terminal Newton ideal and multiplication by \(R^{-n}\) preserves
that ideal. The finite triangular formula for \(U_\pm\), followed
by \(V_n=U_{\operatorname{sgn}n}^{|n|}\), gives bounded-degree
rational \(q\)-coefficients and polynomial size for fixed degree.
Its fixed normals have the same polynomial scope.

Move such exact known columns to the right of (1), without dividing
by their values. A tensor component with a known factor and other
unknown factors is not wholly known; retain it or use an explicit
bounded-degree identity with retained channels. Literal
\(T(R^n\cdot)\) channels are different: their constant input is
\(G_{-n}=T(R^n)\), not a polynomial-budget constant.

The conjugated finite-band operator coefficients have no varying
\(\kappa\) carrier. If a row normalization includes a nonzero scalar
carrier, undo it on the entire equation. Actual source phases remain
on its right side. These conventions give integer Laurent powers
in (3); a presentation with fractional \(q\)-powers may first enlarge
its formal \(q\)-variable.

## 2. The physical monomial trajectory

Fix
\[
 0<a/b<1/2,\quad \gcd(a,b)=1,\quad
 \zeta=e^{2\pi ia/b},\qquad j_N=\lfloor Na/b\rfloor .
 \tag{4}
\]
Restrict to a residue class whose modulus fixes \(N\bmod b\) and all
retained parity factors. A larger modulus may retain the exact source
carrier phases as in the conditioning theorem. Then
\[
 v_{j_N}=\zeta q^\delta,\qquad
 \delta=2\lfloor Na/b\rfloor+1-2Na/b=p'/b',\quad
 \gcd(p',b')=1,\quad b'>0 .
 \tag{5}
\]
At \(\delta=0\), use \(p'=0,b'=1\). Shifted rows use
\(q^{2k}v_{j_N}\); those shifts are already in the matrix (3).
Define
\[
                  \mathfrak b=v^{b'}-\zeta^{b'}q^{p'} .
 \tag{6}
\]
Negative \(p'\) is allowed. An exact classical hit gives
\(\mathfrak b=v-\zeta\).

**Lemma 1.** The substitution
\[
                         q=t^{b'},\qquad v=\zeta t^{p'}
 \tag{7}
\]
has kernel \((\mathfrak b)\) on (3), with all other symbols unchanged.

*Proof.* Since \(q,v\) are units, division using (6) reduces any
Laurent polynomial, modulo \((\mathfrak b)\), to
\[
                 \sum_{k=0}^{b'-1}a_k(h,q,\mathbf w,\mathbf p)v^k .
 \tag{8}
\]
After (7), the \(t\)-exponents in summand \(k\) are congruent to
\(p'k\bmod b'\). These are distinct residue classes, so the
substituted sum is zero only when all \(a_k=0\). The converse is
immediate. This also proves that \(\mathscr R/(\mathfrak b)\)
is a domain. It does not reduce any nilpotent source channel.
\(\square\)

## 3. Two independence statements

**Lemma 2.** For distinct rational \(\lambda_\nu\), a finite sum
\[
                       \sum_\nu A_\nu(h)e^{\pi i\lambda_\nu h},
 \tag{9}
\]
with polynomial \(A_\nu\), vanishes on infinitely many \(h=1/N\to0\)
only if every \(A_\nu=0\). The statement holds coefficientwise in
additional independent polynomial variables.

*Proof.* The sum is entire, so these zeros first imply an analytic
identity. To isolate a candidate term \(\nu\), apply
\[
 \prod_{\mu\ne\nu}
          (\partial_h-\pi i\lambda_\mu)^{\deg A_\mu+1}.
 \tag{10}
\]
Every other term vanishes. The induced operator on \(A_\nu\) is
a product of \(\partial_h+\pi i(\lambda_\nu-\lambda_\mu)\).
Each is invertible on finite-dimensional polynomial spaces because
its diagonal constant is nonzero. Thus \(A_\nu=0\).
For Laurent powers of \(h\), first multiply by a power of \(h\).
\(\square\)

**Lemma 3.** Let \(A(\mathbf w,\mathbf p)\) be a polynomial over a
characteristic-zero coefficient field with
\(\deg_{w_i}A\le d_i\). At each fixed level \(N>\max_i d_i\),
the substitution
\[
                              p_i=P_N(w_i)
 \tag{11}
\]
is injective on this coefficient space.

*Proof.* For one pair, write \(A=\sum_{\ell=0}^L a_\ell(w)p^\ell\),
where \(\deg a_\ell\le d<N\). If \(a_L\ne0\), its substituted term
has leading degree \(NL+\deg a_L\), since \(P_N\) is monic.
Every smaller \(\ell\) has degree at most \(N(L-1)+d<NL\).
Thus the substituted polynomial cannot vanish.

For several pairs, regard the other variables as coefficients.
The highest resulting \(w_1\)-degree has a nonzero coefficient in
the remaining pairs. Apply the same argument successively to that
coefficient for \(w_2,\ldots,w_s\). Substitution in one pair does
not increase the coefficient degree bounds in the others. This is
the lexicographic highest-degree argument and proves injectivity.
\(\square\)

Only the monicity and degree \(N\) of \(P_N=2T_N(w/2)+2\) are used.
No independence at unrestricted coefficient degrees is asserted.

## 4. Generic rank of the actual physical window

Let \(\mathsf A\) be the matrix (3) with \(d\) unknown columns.
For each full-column minor \(D\), set
\[
 \begin{split}
 D^{\rm mic}(h,\boldsymbol\alpha)=D\bigl(
 &h,e^{\pi ih},\zeta e^{\pi i\delta h},\\
 &\{2\cosh(\alpha_i h)\},\{4\cosh^2(\alpha_i/2)\}\bigr).
 \end{split}
 \tag{12}
\]
A fixed power of \(h\) removes its Laurent pole at zero.

**Theorem 4.** The following conditions are equivalent:

1. Every \(D^{\rm mic}\) is the zero meromorphic germ in
   \(h,\boldsymbol\alpha\).
2. Every actual full-column minor \(D\) is divisible by
   \(\mathfrak b\) in (3).
3. The matrix has rank less than \(d\) over
   \(\operatorname{Frac}(\mathscr R/(\mathfrak b))\).

If they fail, an actual minor has a nonzero leading \(h\)-coefficient
as an analytic function of the independent microscopic parameters.
On each compact unit chart for that coefficient, the exact window
has the polynomial conditioning and supplied-data bound of the
pinned conditioning theorem.

*Proof.* Lemma 1 and the usual full-column minor criterion over a
field give \(2\Longleftrightarrow3\); \(2\Longrightarrow1\) is direct.

Suppose \(D^{\rm mic}=0\). At every sufficiently large physical
level in the residue class, vanishing on an open microscopic
parameter set implies the polynomial identity
\[
           D(h_N,q_N,v_{j_N},\mathbf w,\{P_N(w_i)\})=0 .
 \tag{13}
\]
Each nonconstant holomorphic map
\(\alpha_i\mapsto2\cosh(\alpha_i/N)\) has an open image, and the
parameters are independent. The bounded \(w_i\)-degrees of \(D\)
are less than \(N\) for all large levels. Lemma 3 therefore makes
every coefficient of \(D\) in \(\mathbf w,\mathbf p\) vanish at
\((h_N,q_N,v_{j_N})\).

After (5), each such coefficient is a finite sum of Laurent powers
of \(h\) times exponentials with rational exponents. Lemma 2 and
the infinite level subsequence show it is the zero exponential
polynomial. Group equal exponents. Equivalently, the coefficient
is zero after the formal substitution (7), with \(h,t\) independent:
distinct \(t\)-powers give exactly the distinct exponential
frequencies. Lemma 1 makes it divisible by \(\mathfrak b\).
This holds coefficientwise in \(\mathbf w,\mathbf p\), proving 2.

If a minor is not divisible by \(\mathfrak b\), the same argument
makes (12) a nonzero meromorphic germ. Remove its finite \(h\)-pole.
Its first nonzero Taylor coefficient in \(h\) is a nonzero analytic
function of \(\boldsymbol\alpha\). Restrict to a compact set where
that coefficient is a unit and use the exact minor inversion in
the pinned conditioning theorem. \(\square\)

In fact, if a fixed minor is not divisible by \(\mathfrak b\), its
microscopic specialization is not identically zero in the parameters
at any sufficiently large physical level in this residue class.
One formal coefficient has a nonzero finite-order germ on the
trajectory, so is nonzero at every small positive \(h=1/N\);
Lemma 3 applies at each such level. This is generic nonvanishing,
not nonvanishing at every parameter value.

## 5. The remaining source obligation

All minors above belong to the specified actual finite-level window.
They are not inferred from a principal scalar certificate. Small
quantum terms remain. Known source columns can change the proper
unknown matrix, which is why their exact removal precedes the test.

A common divisor may be introduced by a physical nonunit clearing.
The theorem detects it but does not authorize canceling it in the
physical quotient. Failure of rank for this window does not prove
global source nonuniqueness or participation of an exceptional mode.
The other recovery and original closing constraints remain in force.

For constrained parameter subfamilies beyond literal identifications,
retain their algebraic relations explicitly, or use the polarized
generic theorem without asserting rank on the subfamily. Bounds for
the actual holomorphic source may extend by a separate parameter
argument; that is not an assertion of rank on the specialization.

Passing the criterion costs a power of \(N\) on a parameter unit
chart, but still uses the actual supplied packets in (1). Their
largest exponential budget is not reduced. A right packet known
only at a global ceiling does not become an incoming-rate packet.

The unresolved algebraic question is therefore explicit: after the
source-safe reductions, can the complete actual minors have the
common divisor (6) on a resonant physical trajectory? This note
does not exclude it for all products or cores, give a global
repeated-turn rate, or establish a geometric gap.

## 6. Direct sources

The complete direct texts were read at these pins, with their
used implications and hashes checked:

* [Full-step repeated-turn interface](research_full_step_repeated_turn_tensor_interface.md),
  SHA256 ef851eab40c8b2c44388a41d324e2fa41d4400f0f2118fe587405911e00e3398:
  exact rows, bounded-degree rational construction, full normals,
  and retained source and recovery data.
* [Physical-window conditioning](research_resonant_physical_window_conditioning.md),
  SHA256 f1af212ec05ffdb79cc9b99ce03961622740d58622213e648918000e81e5fa07:
  residue trajectories, actual packet accounting, minor inversion,
  and supplied-boundary budgets.
* [Original finite-band turn operators](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb:
  exact conjugation, turn group law, terminal Newton ideals and
  fixed-degree flag preservation.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test or build was
run. Adopted notes and public manuscripts are unchanged.

