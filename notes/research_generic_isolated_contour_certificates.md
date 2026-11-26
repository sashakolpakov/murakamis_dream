# A parameterized contour certificate for isolated nonzero fillings

The contour problem at an isolated vertex depends on its degree and
crossing power, not on the rest of the tangle tree. This note gives one
certificate procedure for those two integers. It also fixes the
logarithmic continuation along the geometric cone deformation.

The finite source is
\[
 P_{d,n,N}(\mathbf u)
   =\phi_N^{(t)}
       \left[R^n\prod_{j=1}^dK_N(t,u_j)\right],
 \qquad
 \Psi_{d,n}(x,t)
   =d\{b(x,t)+b(x,0)\}+\frac{int^2}{4\pi}-it.
 \tag{1}
\]
Here \(d\ge3\) and \(n>0\) are fixed integers. The Newton phase
\(b\), its continued factorial primitives, and the exact trace
normalization are those of
[the scaled contour lifting theorem](research_scaled_wire_contour_lifting.md).
Negative powers are recovered by coefficient conjugation.

The analytic small-saddle theorem already covers
\(d^2+n^2\ge\max(1024,128d)\). The complementary set is
\[
 \mathscr R=\{(d,n)\in\mathbb Z^2:
       d\ge3,\ n\ge1,\ d^2+n^2<\max(1024,128d)\}.
 \tag{2}
\]
It contains exactly \(6\,369\) pairs. The same verifier has now
certified all nineteen contour domains at every pair, with no
failures. An independent archive check reconstructed every rational
subdivision and verified complete parameter coverage, all surface
identifiers and all proof-engine hashes. Thus the argument below,
together with the existing analytic region, supplies the full
boundary-source theorem for every fixed \(d\ge3,n>0\).
The other degrees and zero powers are assembled in
[the all-isolated-filling theorem](research_isolated_vertex_coverage_and_assembly.md).

## 1. The algebraic saddle retains the original angular charge

Put \(w=e^{it/2}\). Define the Gaussian-integer polynomial
\[
 p_{d,n}(w)=(-i)^d(w+i)^d+w^n(w-i)^d.
 \tag{3}
\]
The verifier proposes a root by solving the real cone equations, then
replaces that proposal by an exact rational complex center \(w_0\).
It accepts the disk \(|w-w_0|\le2^{-100}\) only after proving
\[
 |a_0|+\sum_{j\ge2}|a_j|\,2^{-100j}
                    <|a_1|\,2^{-100},
 \qquad
 p_{d,n}(w_0+z)=\sum_j a_jz^j.
 \tag{4}
\]
Rouché's theorem gives exactly one simple root in that disk.
The coefficients in (3) are constructed as exact integer pairs;
floating-point root finding has no role in acceptance.

On the resulting enclosure define
\[
 t=-2i\log w,\qquad
 x=\frac1\pi\arctan\cos(t/2),\qquad
 y=-i\,\frac{w+i}{w-i}=\sec(t/2)+\tan(t/2).
 \tag{5}
\]
The principal functions in (5) are analytic on the recorded
enclosures. The verifier proves
\[
 \begin{gathered}
 0<\Re t<\min(\pi/2,2\pi/n),\qquad \Im t<0,\\
 \alpha<\Re x<\tfrac12-\alpha,\qquad
 0<\Im x<-\Im t/(2\pi),\\
 \tfrac12-\Re x-\Re t/(2\pi)>0,\qquad
 \Re y>0,\quad \Im y<0.
 \end{gathered}
 \tag{6}
\]
The last inequality in the second line fixes the opposite factorial
sides used by the contour. The third line places the saddle itself
strictly in the ordinary factorial bulk.

Equation (3) says \(y^d=-w^n\). Consequently
\[
 \exp\left(d\log y-\frac{int}{2}+i\pi\right)=1.
 \tag{7}
\]
The verifier also encloses the expression in parentheses in a disk
of radius \(1/100\). An integer multiple of \(2\pi i\) in that disk
is zero. Thus it certifies the original, unexponentiated cone equation
\[
          d\log\{\sec(t/2)+\tan(t/2)\}
                          =\frac{int}{2}-i\pi,
 \tag{8}
\]
with unit angular charge. This is stronger than merely locating a
zero of the polynomial (3). By the uniqueness proof in
[the geometric branch theorem](research_isolated_internal_vertex_geometry.md),
this is the selected positive branch.

For the literal continued phase (1), the same root equations give
\[
              e^{\Psi_x/d}=1,\qquad e^{2\pi\Psi_t}=1.
 \tag{9}
\]
The verifier bounds both \(|\Psi_x|\) and \(|\Psi_t|\) by \(1/100\).
The possible nonzero logarithmic values in (9) are thereby excluded,
so \(\Psi_x=\Psi_t=0\) exactly.

## 2. Continuation of the factorial sides along the cone deformation

The selected endpoint must also have the same phase normalization
as the complete structure. This does not require that every
factorial argument have positive real part throughout the deformation.
Its side of the logarithmic cut must instead remain fixed.

Write the original cone branch as
\[
 t(\lambda)=2a-2ib,\qquad
 0<a<\pi/2,\quad b>0,\quad 0<\lambda\le1.
 \tag{10}
\]
The geometric branch proof gives
\[
 \sin a=\cosh b\,\tanh(nb/d),\qquad
 na+d\,\arctan\frac{\sinh b}{\cos a}=\pi\lambda.
 \tag{11}
\]
We claim that \(a<\pi/4\) whenever \(d\ge3\).
If \(n\ge4\), this follows at once from \(na<\pi\lambda\).
Otherwise \(n\le3\le d\), and the first equation gives
\(\sin a\le\sinh b\). Hence
\[
 \arctan(\sinh b/\cos a)\ge a,\qquad
 (n+d)a\le\pi\lambda.
 \tag{12}
\]
Here \(n+d\ge4\). Equality at the only borderline integer pair,
\((d,n)=(3,1)\), is impossible because
\(\tanh(b/3)<\tanh b\) for \(b>0\). This proves the claim.

Let
\[
       \theta+i\beta=\arctan\cos(a-ib).
 \tag{13}
\]
Since \(\cos(a-ib)\) has positive real and imaginary parts,
the principal arctangent has \(0<\theta<\pi/2\) and \(\beta>0\).
Its imaginary part satisfies the exact identity
\[
 \tanh(2\beta)
   =\frac{2\sin a\,\sinh b}{\cosh^2b+\cos^2a}.
 \tag{14}
\]
The arithmetic-geometric mean inequality gives
\[
 \tanh(2\beta)
 \le \tan a\,\tanh b
 <\tanh b.
 \tag{15}
\]
The strict inequality uses \(a<\pi/4\). Since the hyperbolic tangent
is increasing on the real line, \(2\beta<b\). Thus, with
\(x(\lambda)=(\theta+i\beta)/\pi\),
\[
 \begin{split}
 \Im\left(\tfrac12-x+\frac{t}{2\pi}\right)
                         &=-(\beta+b)/\pi<0,\\
 \Im\left(\tfrac12-x-\frac{t}{2\pi}\right)
                         &=(b-\beta)/\pi>0.
 \end{split}
 \tag{16}
\]
The first denominator stays strictly below its cut and the second
strictly above it, for the entire positive cone path. The parent
denominators \(\tfrac12-x\) have positive real part because
\(0<\theta<\pi/2\). At \(\lambda=0\), \(t=0\), \(x=1/4\), and
the branches begin at the complete normalization. Equations
(14)–(16) therefore fix the absolute continuation of (1).
Positive real parts at the final saddle are checked separately
in (6).

This distinction matters. A bound on \(\cosh b\) alone does not
prove that the real parts of all factorial arguments remain
positive. No such assertion is used here.

## 3. The nineteen contour inequalities

Set \(h_t=-\Im t_*>0\), \(h_x=\Im x_*>0\), and
\(M=\Re\Psi_{d,n}(x_*,t_*)\). Take \(T=2\pi/3\).
The verifier checks exactly the nineteen surfaces in
[the degree-two certificate](research_internal_degree_two_contour_certificates.md),
Section 2, with the following systematic replacement:
every wire penalty \(4\pi h_x v\) becomes \(2\pi d h_xv\),
and similarly for the independent product \(vs\) on nested
endpoint surfaces. The shared charge \(-it\) remains unchanged.

The full \(d\)-wire exponent obeys the exact identity
\[
 \Re\mathcal F_{d,n}(\mathbf x,t)-\sum_jp_j
    =\frac1d\sum_j
          \{\Re\Psi_{d,n}(x_j,t)-dp_j\}.
 \tag{17}
\]
A scaled gap \(\delta\) on one nonprincipal wire consequently
gives an actual gap at least \(\delta/d\). The sign and scaling
of each penalty are part of the verifier, including its gradient
in the Taylor bounds. Nested endpoint surfaces are evaluated
directly with both independent depth parameters, so their mixed
product is retained.

The main upper-wire rectangle is split into a rational rectangle
around the saddle and its complement. A \(24\)-by-\(24\)
subdivision certifies a negative definite real Hessian on the
local rectangle. Its angular width decreases when the positive
critical angle is small; it never crosses the boundary
\(\Re t=0\). The complement has the strict gap
\[
                  \frac{1}{10^6(d+n)^4}.
 \tag{18}
\]
The negative-angle and lower-wire rectangles have gap
\(1/[100(d+n)^4]\). Each angular-cutoff and endpoint rectangle
has gap \(1/1000\). The reports contain the rational cover and
its accepted outward bounds for each pair.

Only the trace-first surfaces occur. In particular, no estimate
is inferred for an interior trace angle with an independently
varying angular height. The exact lifting proof does not generate
that extra family.

## 4. Uniform finite-source inputs and the result of a successful run

For a common run over the remaining integer parameters, use
\[
                     \alpha=1/128,\qquad\beta=63/128.
 \tag{19}
\]
[The uniform wire-gap theorem](research_uniform_isolated_wire_gap.md)
gives a gap greater than \(1/60\) for the original contribution
with at least one wire outside (19). This bound retains high
indices, original first normals, and all real free-boundary
angles. The verifier also checks the corresponding action
inequality directly at every supplied pair.

[The all-degree angular theorem](research_all_degree_outer_angle_gap.md)
gives \(M>5d/6\), whereas each retained wire subset at the real
cutoff has rate below \(4/5\). Thus the original outer trace
contribution has a gap greater than \(d/30\), including its first
normal at polynomial cost.

The finite-factorial domains are uniform. On the wire contours
the smallest normalized real part of a continued denominator is
\[
                    \alpha-\frac13=-\frac{125}{384}>-\frac12.
 \tag{20}
\]
The numerator arguments lie between \(1/6\) and \(5/6\).
The corresponding real parent arguments lie between
\(-\beta\) and \(1-\alpha\). The existing reciprocal-factorial
estimates cover these ranges, including their zeros. The
inequality \(h_t>2\pi h_x\) gives the required opposite sides
throughout every nested rectangle. At the saddle, (6) supplies
the ordinary nonzero bulk expansion. Half-grid endpoint
displacements are \(O(N^{-1})\); the fixed strict gaps persist
by the uniform logarithmic modulus estimates already used in
the lifting theorem.

Consequently, for every pair whose complete report passes, the
lifting theorem proves
\[
 P_{d,n,N}(\mathbf u)
   =C_{N,n}N^{-3(d-1)/2}
        A_{d,n}(\mathbf u)e^{N W_{d,n}(\mathbf u)}
                          (1+O(N^{-1})),
 \tag{21}
\]
on a fixed complex neighborhood of complete boundary angles.
The amplitude is holomorphic and nonzero there. The same theorem
provides the bound for all real free-boundary angles and its
Gaussian extension to a thin complex strip. Equations (8) and
(16) identify the selected action with the original geometric
branch, with the existing primitive marking. The degree and
crossing power are fixed before \(N\) tends to infinity; no
uniform asymptotic error in unbounded \(d,n\) is asserted.

## 5. Reproduction and complete finite coverage

The parameterized verifier is
[certify_isolated_vertex_scaled_contours.py](../experiments/certify_isolated_vertex_scaled_contours.py).
It calls the audited degree-two phase engine with the new exact
root polynomial, degree-scaled phase and penalties, and a local
rectangle adapted to the critical angle. The
[complete manifest](../repro/results/research-isolated-scaled-all-manifest.json)
records every accepted pair and the exact hash of its compressed
certificate. Every pair uses (19).

The existing small-saddle theorem applies whenever
\[
                    d^2+n^2\ge\max(1024,128d).
 \tag{22}
\]
There are exactly \(6\,369\) positive integer pairs with
\(d\ge3,n\ge1\) outside (22). They lie in
\(3\le d\le127,\ 1\le n\le63\).
Indeed, \(d\ge128\) implies (22). For \(n\ge64\),
\(d^2+n^2\ge4096>1024\) and
\[
                 d^2+n^2-128d\ge(d-64)^2\ge0.
\]
The driver independently enumerates \(3\le d\le127,\ 1\le n\le127\),
applies the literal complementary inequality, checks that there
are \(6\,369\) distinct pairs, and confirms that its largest power
is \(63\).

[The batch driver](../experiments/batch_isolated_vertex_scaled_contours.py)
runs this unchanged certificate on a supplied degree range. It saves
one compressed certificate per pair and a manifest of their exact
hashes, rather than repeatedly rewriting one large report. Every
pair uses the common interval (19). Its parameter list is the
literal integer inequality complementary to (22); a manifest is
marked complete only after every listed pair has passed. Previously
saved certificates can be reused only when all proof-engine hashes,
the wire interval and sufficient recorded precision agree.
Each successful certificate is written atomically; a failure is
recorded separately and cannot be counted as a success.

The complete run passed all \(121\,011\) surface domains. It used
\(6\,389\,640\) accepted rational boxes, with
\(12\,658\,269\) visited subdivision nodes. It retained every box
in \(6\,369\) compressed certificates. The
[independent archive checker](../experiments/check_isolated_contour_archive.py)
then verified the exact parameter set and all archive hashes.
For each surface it reconstructed the full binary subdivision from
the initial rectangle and its prescribed rational split scale.
It rejected duplicate or unreachable leaves and checked that
every local-Hessian leaf belonged to the main rectangle and lay
inside its certified local neighborhood.
Its [saved result](../repro/results/research-isolated-scaled-all-integrity.json)
confirms all those counts. This archive check is separate from
the outward evaluation of the analytic inequalities; it does not
claim to repeat that evaluation.

To reproduce the whole certificate and its independent coverage check:

    python3 experiments/batch_isolated_vertex_scaled_contours.py \
      --degrees 3 127 --workers 2 \
      --report-directory repro/results/research-isolated-scaled-all-pairs \
      --manifest repro/results/research-isolated-scaled-all-manifest.json
    python3 experiments/check_isolated_contour_archive.py \
      --manifest repro/results/research-isolated-scaled-all-manifest.json \
      --output repro/results/research-isolated-scaled-all-integrity.json

The proof-engine hash is

    7575986de0b96523d481ece8bba0f26597c57d1983a5311e01266f9501dc20ed

The manifest and each pair certificate also record the degree-two
phase engine and the underlying interval primitive engine hashes.
The smaller
[pilot report](../repro/results/research-isolated-scaled-contour-pilots.json)
and [small-power report](../repro/results/research-isolated-scaled-small-powers.json)
remain available for quick partial replays; neither substitutes
for the exhaustive archive.

This completes the finite remainder for isolated short-filled
vertices. Adjacent short-filled components require their own
source argument. In particular, the theorem does not imply
finitely many exceptional twist assignments for every original
template.
