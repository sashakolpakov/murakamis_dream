# The full original two-boundary packet for an internal pair of powers three

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

This note assembles the exact mixed-source estimates into the
original two-boundary source for adjacent powers \(3,3\), and by
conjugation for \(-3,-3\). It proves a nonzero geometric packet
through both level parities, with the two ordinary boundary
variables and all original first-normal data retained. It also
proves a strict angular bound over the whole outside periods
and its quadratic extension to a fixed complex strip.

The result concerns this fixed short block. It does not assert
stability under every short partial filling or the general
finite-exception theorem.

## 1. Original source and statement

Use the original circle-tree Newton kernel, crossing and trace.
The two selected vertices have original degrees two, and their
three incident edges form a path between the two free endpoints.
The exact source is
\[
 \mathcal P_N(u,v)=
   \phi_N^{(t)}\phi_N^{(r)}
       [R(t)^3R(r)^3K_N(u,t)K_N(t,r)K_N(r,v)].
 \tag{1}
\]
The trace includes the first normal at each double spectral
root and the value at the odd-level simple root. Only the two
selected variables are reduced in their physical algebras.
The source has degree at most \(N-1\) in each ordinary boundary
variable \(-2\cos u,-2\cos v\).
The original disk frames and carriers are fixed; in a filling
presentation its selected powers mean \(n_v=\eta_v-2p_v=3\),
with those original primitive curves.

Let \(W_{3,N}(x,u)\), \(S(x,u)\), \(A(x,u)\), and \(x_*\)
be the exact mixed source and local packet of
[the mixed-polarization theorem](research_internal_pair_three_mixed_packet.md).
In particular,
\[
 W_{3,N}(x,u)=C_{N,3}N^{-1}A(x,u)e^{NS(x,u)}
                       (1+O(N^{-1})),\qquad
 C_{N,3}=e^{3\pi i(N-1)^2/(4N)}.
 \tag{2}
\]
At \((x,u)=(x_*,0)\), \(S_x=0\), \(\Re S_{xx}<0\), and
\(A\ne0\).
The implicit-function theorem defines a unique local
\(x=x(u,v)\) through \(x_*\) by
\[
              S_x(x,u)+S_x(x,v)=0.
 \tag{3}
\]
Put
\[
 \begin{split}
 \mathcal S(u,v)&=S(x(u,v),u)+S(x(u,v),v),\\
 \mathcal A(u,v)&=
  \frac{\sqrt{2\pi}\,A(x(u,v),u)A(x(u,v),v)}
       {\sqrt{-S_{xx}(x(u,v),u)-S_{xx}(x(u,v),v)}},\\
 M_{\rm pair}&=\Re\mathcal S(0,0)
                  =2\Re S(x_*,0).
 \end{split}
 \tag{4}
\]
The square root is fixed at the base point by the convergent
horizontal Gaussian and then continued holomorphically.

**Theorem 1.** On a fixed complex bidisk about \((0,0)\),
\[
 \boxed{\quad
 \mathcal P_N(u,v)
   =C_{N,3}^{\,2}N^{-3/2}\mathcal A(u,v)
          e^{N\mathcal S(u,v)}(1+O(N^{-1})).
 \quad}
 \tag{5}
\]
The amplitude is holomorphic and nonzero. The normalized
remainder is holomorphic, and each fixed boundary derivative
has the corresponding estimate on smaller bidisks. Both
parities of \(N\) are included. All sufficiently large levels
therefore have a nonzero complete-boundary leading term.

The phase is separately even and has
\[
 \partial_{uu}\mathcal S(0,0)
 =\partial_{vv}\mathcal S(0,0)
       =-\frac{\cos(t_*/2)}{2\pi},\qquad
 \partial_{uv}\mathcal S(0,0)=0.
 \tag{6}
\]
Its real boundary Hessian is negative definite.
Here \(t_*\) is the actual geometric angle enclosed in the
mixed-polarization theorem. There are also positive
\(c,B,b,C\) and a finite exponent \(a\), independent of \(N\),
such that
\[
 \begin{split}
 |\mathcal P_N(u+is,v+it)|
 \le C N^a \exp N\bigl\{
 M_{\rm pair}
 -c(1-\cos u)-c(1-\cos v)+B(s^2+t^2)\bigr\}
 \end{split}
 \tag{7}
\]
for real \(|u|,|v|\le\pi\) and \(|s|,|t|\le b\).

The phase in (5) is the original marked stationary action,
including all three edge constants. At the complete boundaries,
\[
              2\pi\Re\mathcal S(0,0)
                 =\operatorname{Vol}Y_{3,3},
 \tag{8}
\]
where \(Y_{3,3}\) is the original positive partial filling
with its two outside cusps complete. This is a statement
about the partial-exterior source (1); a separate closing
operation must still keep its original scalar and framing.

## 2. Exact circle averaging and the whole cycle

The full-Hermite interpolation gives exactly
\[
 \mathcal P_N(u,v)
       =N\int_{iY}^{1+iY}
              W_{3,N}(x,u)W_{3,N}(x,v)\,dx,
 \qquad Y=\Im x_*.
 \tag{9}
\]
Each factor has the half-band
\(\{-(N-1)/2,\ldots,(N-1)/2\}\). Its product therefore
has integer frequencies in \([-(N-1),N-1]\); its \(N\)-point
sum is precisely \(N\) times its constant Fourier
coefficient. This proves (9), at both parities, with no
internal-index alias or normal correction omitted.
It is an exact identity in both free boundary polynomials.

The same height \(Y\) is used in four contiguous portions:

| Real internal coordinate | Proved estimate |
|---|---|
| \(0\le\Re x\le7/100\) | [Left complement](research_internal_pair_three_low_wire_complement.md) |
| \(7/100\le\Re x\le3/10\) | [Central interval and packet](research_internal_pair_three_mixed_packet.md), Section 7 |
| \(3/10\le\Re x\le1/2\) | [Right complement](research_internal_pair_three_right_period.md) |
| \(1/2\le\Re x\le1\) | [High half-period](research_internal_pair_three_high_half_bound.md) |

Each complementary portion has a strict rate gap below
\(M=\Re S(x_*,0)\), uniformly on a common small complex
outside-boundary disk. The central theorem proves the same
gap outside a small neighborhood of \(x_*\), and retains
the actual nonzero local packet there.
All four estimates use the original source. In particular,
the complement proofs retain the outer Newton index in its
real finite sum and move only the trace contour; they do
not assume an unproved complex bare-kernel expansion.

Their finite proofs account for both original discarded
regions: outer wire indices outside \([1/32,15/32]\), and
physical trace rows outside the angular cutoff. The retained
trace has its full double-pole charge kernel and exact
angular endpoint currents. In the central portion its
remaining outer-wire contour also retains all nineteen
logical surfaces, split into thirty-one domains where the
fixed internal factorial changes side. Thus the bounds
control the entire complement in (9), not only competing
stationary points.

It follows that the product in (9), outside the local
neighborhood, has a strict gap below \(2M\).
Near \(x_*\), insert (2). The Gaussian in the single
shared coordinate gives
\[
 \int e^{N\{S(x,0)+S(x,0)-2S(x_*,0)\}}\,dx
       \sim \sqrt{\frac{\pi}{-N S_{xx}(x_*,0)}}.
 \tag{10}
\]
The total power is \(N\cdot N^{-2}\cdot N^{-1/2}=N^{-3/2}\),
and the exact level scalar is \(C_{N,3}^2\).
Its amplitude is
\[
          \mathcal A(0,0)
               =\sqrt{\frac{\pi}{-S_{xx}(x_*,0)}}A(x_*,0)^2
               \ne0.
 \tag{11}
\]
There is only one leading contribution in this representation;
the finite-source bounds have already controlled every other
part of its actual cycle.

For small complex \(u,v\), use (3) and deform the local
neighborhood to its holomorphic critical point. The strict
complement gaps persist after shrinking the bidisk.
Uniform analytic Gaussian expansion proves (5), with the
coefficient (4). Cauchy's formula gives all fixed derivatives.
Separate evenness descends the statement to ordinary
spectral coordinates at \(-2\), retaining the endpoint
normal data rather than only angular values.

## 3. Original geometry and boundary curvature

Before stationary elimination, the phase of the two factors
in (9) is
\[
 \begin{split}
 &b(x,t)+b(y,t)+b(y,u)
   +b(x,r)+b(z,r)+b(z,v)\\
 &\hspace{25mm}
   +\frac{3i(t^2+r^2)}{4\pi}-i(t+r).
 \end{split}
 \tag{12}
\]
The three wire stationary equations give precisely
\(\psi(t,r)\), \(\psi(t,u)\), and \(\psi(r,v)\).
Consequently its critical value is that of
\[
 \psi(t,r)+\psi(t,u)+\psi(r,v)
                +\frac{3i(t^2+r^2)}{4\pi}-i(t+r).
 \tag{13}
\]
The branch and absolute constant agree with the complete
structure, as proved in Section 2 of the mixed-packet note.
At \(u=v=0\), the selected point is the unique positive
internal \(3,3\) solution of the
[marked pair geometry](research_radical_path_sector_gap.md),
Theorem 5. The original
[positive-point marked completion](research_positive_point_marked_completion.md)
and [pointwise volume identity](research_positive_edge_volume_identity.md)
give (8).
The small-boundary germ in (13) keeps those same primitive
meridians, disk longitudes and original carriers.

Every first \(u\)-derivative of (12) vanishes at \(u=0\),
including its derivatives in the internal variables.
Thus implicit stationary differentiation contributes no
Schur correction to the boundary Hessian at zero.
The only term is
\[
              b_{uu}(y_*,0)
                  =-\frac{\tan(\pi y_*)}{2\pi}
                  =-\frac{\cos(t_*/2)}{2\pi}.
 \tag{14}
\]
The same calculation applies to \(v\), and there is no
mixed \(u,v\) term. The real part of \(\cos(t_*/2)\) is
strictly positive, proving (6).

## 4. The whole outside period and its complex strip

The source estimates have more information than their
small-boundary formulations. In every retained contour
term, the outside angle occurs in the factor \(B_N(y,u)\),
where
\[
             1/32\le\Re y\le15/32,\qquad |\Im y|\le k,
             \qquad k=\Im y_*.
 \tag{15}
\]
On the complementary internal-circle portions the outer
wire stays real, which is a subset of (15).
The uniform reciprocal-factorial inequality gives
\[
 \mathfrak b(y,u)-\mathfrak b(y,0)
    \le-c_0(1-\cos u),\qquad
 c_0=\frac{\sin(\pi/16)}{4\pi\cosh^2(\pi k)}>0,
 \tag{16}
\]
for every real \(|u|\le\pi\). It keeps every moving
reciprocal zero. The relevant branches and exact factorials
are those of
[the uniform boundary-decay theorem](research_uniform_factorial_and_boundary_decay.md).

The estimate extends, after decreasing the angular constant,
to fixed small complex heights:
\[
 |B_N(y,u+is)|
  \le C N^a\exp N\{
      \Re b(y,0)-c_1(1-\cos u)+B_1s^2\}.
 \tag{17}
\]
This is the exact factorial strip estimate in Section 2 of
[the cardinal/factorial comparison](research_free_boundary_cardinal_factorial_comparison.md);
its proof of that estimate precedes any polynomial
interpolation. On the compact wire rectangle (15), the
constants are uniform. Near \(u=0\), \(b_u(y,0)=0\);
completion of the mixed real-imaginary quadratic term
gives (17). Away from zero the fixed real angular loss
survives a sufficiently thin strip. No value-only
interpolant is substituted in this argument.

Applying (17) on each retained source contour gives its
old bound with the additional loss
\(-c_1(1-\cos u)+B_1s^2\). This applies equally to
principal terms, rational charge corrections and endpoint
currents. They all contain the same retained parent factor.
The small-depth collar can also be estimated before any
wire expansion, with that factor at its original real
index.

The two discarded original finite regions require a
separate argument. Their real-boundary estimates were
uniform in \(|u|\le\pi\): low Newton factors obey their
full interval bound, and the high Newton sector obeys
the original polynomial Hermite bound. Each such error
has rate at most \(M-\delta\) for a fixed \(\delta>0\),
uniformly over the compact internal-circle portions.
Since these errors are still degree-at-most-\(N-1\)
polynomials in \(-2\cos u\), Fourier/Chebyshev continuation
gives
\[
 |E_N(u+is)|\le C N^a e^{N(M-\delta+|s|)}.
 \tag{18}
\]
This applies only to the original finite errors; no
polynomial assumption is made about a separate
off-grid contour integrand.
Choose \(b\le\delta/4\) and \(c\le\delta/4\).
Then \(1-\cos u\le2\) shows that (18) is bounded by
\[
                 C N^a e^{N\{M-c(1-\cos u)\}},
                  \qquad |s|\le b.
 \tag{19}
\]
There are finitely many error types, so take common
positive minima, also with \(c\le c_1\).

Combining (17)--(19) and all the exact contour estimates
gives the uniform whole-circle bound
\[
 \sup_{0\le a\le1}|W_{3,N}(a+iY,u+is)|
 \le C N^p
       e^{N\{M-c(1-\cos u)+B s^2\}}.
 \tag{20}
\]
Here \(p\) is a fixed exponent, independent of the real
circle coordinate.
Using (20) for the two factors in (9) proves (7).
This is an upper bound; the lower asymptotic comes from
the separately established nonzero Gaussian in Section 2.

All physical first normals remain covered. On a disk of
angular radius \(1/N\), Cauchy's inequality adds only
powers of \(N\) to (17) or (20), with a bounded change
in the exponent. At a double physical node
\(|\sin u|\ge\sin(\pi/N)\), so the angular-to-spectral
derivative costs another polynomial factor. The odd
simple node requires only its value. At the complete
ordinary boundary, the separately even local expansion
in Section 2 supplies every spectral derivative.

## 5. Mirroring and scope

All kernel polynomials and the Frobenius trace have real
coefficients, and the original negative crossing is the
coefficientwise conjugate of the positive one.
Therefore the \(-3,-3\) source is exactly
\[
        \mathcal P_N^{-}(u,v)
                 =\overline{\mathcal P_N(\bar u,\bar v)}.
 \tag{21}
\]
Its phase and amplitude are the corresponding holomorphic
conjugates, and its exact level scalar is
\(\overline{C_{N,3}^{\,2}}\). All conclusions, including
the whole-period strip bound and primitive boundary data,
follow without changing a level-parity convention.

The proof uses no positivity assertion for the same-sign
bilinear coefficient vector. The nonzero contribution is
selected on the exact complex Fourier circle, and all
other parts of that circle are bounded before the local
Gaussian is applied. The result supplies this particular
adjacent short block with the retained analytic boundary
data needed in later source compositions. It does not
replace the missing corresponding statements for other
fixed short connected blocks.
The [composition corollary](research_internal_pair_three_kernel_compositions.md)
applies the existing finite-kernel theorem to this result: any fixed
number of these pairs and their mirrors may be separated by eligible
long signed powers, with one common finite threshold.

## 6. Reproducing the finite certificates

From the repository root, run

~~~sh
python3 experiments/reproduce_internal_pair_three.py
~~~

This recomputes the local packet certificate and the central,
left, right, and high-half certificates, using outward interval
arithmetic. The runner also checks the expected complete domain
lists and the hashes of each script and its dependencies.
The five detailed records and their aggregate record are saved
under the repro/results directory.

For a quick check that the saved records match the current sources,
run the same command with the --verify-saved option. That option does
not recompute the interval inequalities. The exact source identities,
contour arguments, geometric normalization, and asymptotic
deductions have the written proofs cited above; the finite
certificates verify their specified numerical inequalities.
