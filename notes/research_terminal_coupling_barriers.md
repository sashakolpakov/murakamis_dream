# Using the neighbouring equations in a terminal rate comparison

Research reduction, 5 November 2026. An independently varying terminal
input permits parameter values that need not occur in an open tangle.
The ordinary block immediately before the terminal block supplies
explicit necessary constraints on that input. This note derives those
constraints and gives a boundary inequality sufficient to prove the
terminal rate comparison on the constrained set.

The boundary inequality is a target for verification, not an assertion
that suitable multipliers have already been found.

## 1. Recovering the preceding leg from the terminal input

Consider an open word of length at least three, with all block types
in \(\{3,4\}\), at its original complete-colour critical point.
Let the penultimate block have type \(3+\alpha\), and the last
block type \(3+\epsilon\), where \(\alpha,\epsilon\in\{0,1\}\).
Use the following four coordinates:

* \(a\) is the penultimate leg directed towards the terminal block;
* \(s\) is the other leg of that same penultimate block;
* \(b\) is the leg of the terminal block directed towards it;
* \(c\) is the external leg preceding the penultimate block.

The terminal map in
[the terminal comparison](research_mixed_terminal_half_endpoint_gap.md)
gives \(b=t_\epsilon(a)\) holomorphically on the original input
disk. Its two other coordinates are the private terminal leg and
the ordinary boundary variable, which need not be recovered here.
Set
\[
 V=e^{-2\pi ia},\qquad B=e^{-2\pi ib},\qquad
 U=e^{-2\pi is},\qquad A=e^{-2\pi ic},\qquad k=2+\alpha.
\tag{1}
\]
The ordinary penultimate block has the original equations
\[
\begin{split}
 0&=g'(s+a)+g'(s+c)-k g'(s)+2\pi ic,\\
 0&=g'(s+a)+g'(a+b)-k g'(a)+2\pi ib.
\end{split}
\tag{2}
\]
These are the ordinary two-leg equations in
[the universal conditional construction](research_mixed_reduced_disk_conditional_packets.md),
with the two external coordinates named \(c,b\). In particular,
the terminal block has not been substituted for an ordinary block.
The assumption on length ensures that the penultimate block is
ordinary rather than the first boundary block.

Since \(g'(z)=\operatorname{Log}(1-e^{-2\pi iz})\),
exponentiating (2) gives
\[
 (1-UV)(1-UA)=A(1-U)^k,
 \qquad (1-UV)(1-VB)=B(1-V)^k.
\tag{3}
\]
Consequently the terminal input determines the functions
\[
 \mathcal U(a)
 =\frac{1-B(a)(1-V(a))^k/(1-V(a)B(a))}{V(a)},
 \qquad
 \mathcal W(a)
 =\mathcal U(a)+\frac{(1-\mathcal U(a))^k}
                         {1-\mathcal U(a)V(a)}.
\tag{4}
\]
At every actual open-word critical point,
\[
                  \mathcal U(a)=e^{-2\pi is},
 \qquad \mathcal W(a)=e^{2\pi ic}=A^{-1}.
\tag{5}
\]

Both functions in (4) are holomorphic throughout the original closed
input disk and on a neighbourhood of it. Indeed \(a,b\in
Q=[.23,.45]+i[-.12,.12]\), so \(0<\Re(a+b)<1\).
Thus \(1-VB\ne0\), and \(V,B,1-V\) are nonzero as well.
The identity
\[
 1-\mathcal U V=\frac{B(1-V)^k}{1-VB}\ne0
\tag{6}
\]
removes the remaining denominator. The functions \(\mathcal U\)
and \(\mathcal W\) themselves may have zeros away from actual
critical inputs; holomorphy does not exclude those zeros.

Only necessary constraints have been derived. Solving (3) does not
restore the original logarithmic lifts, prove that all other blocks
can be attached, or establish a finite-source asymptotic.

## 2. Modulus constraints inherited from the geometric domains

The full-bidisk image estimates in
[the universal height proof](research_mixed_cyclic_critical_height_bounds.md),
Proposition 1 and its proof, give
\[
 \Im s>\ell_\alpha,
 \qquad \ell_0=-13/200,\quad \ell_1=-51/500.
\tag{7}
\]
Although the proposition also states a cyclic-word consequence,
its proof establishes these image bounds on the entire input bidisk
before applying them to a cyclic critical point. They therefore apply
to the ordinary penultimate block here: both of its actual external
legs belong to their original typed disks.

For the preceding external leg \(c\), let its type be \(3+\gamma\).
It is a nonprivate leg, including when it is attached to the first
boundary block in a word of length three. The smaller typed disks
established for the actual open word in
[the local-factor coverage proof](research_mixed_open_local_factor_coverage.md)
give the upper bounds
\[
 \Im c<h_\gamma,
 \qquad h_0=73/1000,\quad h_1=1/125.
\tag{8}
\]
These bounds do not assume that \(c\) is an ordinary interior leg.

By (5), the two continuous constraints at every actual input are
\[
\begin{split}
 \psi_1(a)&:=\log|\mathcal U(a)|-2\pi\ell_\alpha\ge0,\\
 \psi_2(a)&:=\log|\mathcal W(a)|+2\pi h_\gamma\ge0.
\end{split}
\tag{9}
\]
Strict inequalities would hold with the stated strict image bounds;
the weak form is convenient for a closed feasible set. A zero of
either function fails its corresponding constraint.

The advantage of (9) is that it uses no inverse logarithm and no
choice of argument. A violated modulus condition alone excludes an
input. The constraints remain necessary, rather than sufficient.
Neither function is identically zero: existence of an actual
three-block critical point with the specified types supplies a point
where both identities (5) are nonzero. The holomorphic identity
principle gives the same conclusion on every subdomain considered
below.

## 3. A boundary certificate for a constrained minimum

**Lemma 1.** Let \(D\) be a closed disk or rectangle, and let
\(G\) be continuous on a neighbourhood of \(D\) and superharmonic
on its interior. Let \(f_1,\ldots,f_q\) be holomorphic on a
neighbourhood of \(D\), none identically zero, and let \(r_j>0\).
Choose numbers \(\lambda_j\ge0\). Suppose that, on the boundary,
\[
 G(a)-\sum_{j=1}^q\lambda_j\log\frac{|f_j(a)|}{r_j}
                                      \ge\delta.
\tag{10}
\]
A term with \(\lambda_j=0\) is omitted, including at zeros.
A positive coefficient gives the value \(+\infty\) at a zero.
Then
\[
 G(a)\ge\delta
 \quad\text{whenever }a\in D\text{ and }|f_j(a)|\ge r_j
                          \text{ for every }j.
\tag{11}
\]

*Proof.* Each \(-\log|f_j|\) is superharmonic, with value
\(+\infty\) at a zero. Therefore the left side of (10), viewed
as an extended-real function on \(D\), is superharmonic. The
minimum principle gives the same lower bound in the interior.
Equivalently, remove small disks about its finitely many zeros;
near a zero with positive coefficient the function tends to
\(+\infty\), so those new boundary circles cannot lower the
minimum. Let their radii decrease to zero.

At a point satisfying the modulus constraints, all the logarithms
in (10) are nonnegative. Restoring their nonnegative weighted sum
therefore proves (11). \(\square\)

This is a sufficient inequality on an ordinary geometric boundary.
It avoids finding the boundary of the set cut out by several modulus
constraints. It does not guarantee that a successful choice of the
numbers \(\lambda_j\) exists.

## 4. Application to the terminal row envelope

Write \(P_\epsilon(a)\) for the original optimized terminal action,
and \(h_{1/2}\) for the terminal coefficient's rate at the real
half-period. Let \(\mathcal E_\epsilon(a)\) be either the full
absolute row envelope at that half-period or the larger explicit
envelope in
[the all-row theorem](research_mixed_terminal_half_row_envelope.md).
Both envelopes are continuous and subharmonic in the external input.
Thus
\[
 G_\epsilon(a)=\Re P_\epsilon(a)-h_{1/2}
                                      -\mathcal E_\epsilon(a)
\tag{12}
\]
is continuous and superharmonic. Choose a closed disk or rectangle
inside the original holomorphic terminal-map domain. If, for some
\(\lambda_1,\lambda_2\ge0\) and \(\delta>0\),
\[
 G_\epsilon(a)-\lambda_1\psi_1(a)-\lambda_2\psi_2(a)
                                         \ge\delta
                    \quad(a\in\partial D),
\tag{13}
\]
then Lemma 1 proves the half-period rate gap at every actual critical
input in \(D\) with the specified neighbouring types. This remains
valid if the unrestricted gap is negative elsewhere in the disk.

For example, a complete finite covering of \(\partial D\) may
provide lower bounds \(g_i\) for \(G_\epsilon\), and upper bounds
\(u_{ij}\) for \(\psi_j\), on each boundary cell \(i\).
The finite list of linear inequalities
\[
 g_i-\lambda_1u_{i1}-\lambda_2u_{i2}\ge\delta,
 \qquad\lambda_1,\lambda_2\ge0,
\tag{14}
\]
is sufficient for (13). With the explicit maximum of several row
bounds, retain one inequality for each branch on each cell. Rational
candidate multipliers can be checked against outward enclosures;
finding a numerical candidate alone is not a certificate.

If (13) is proved with a strict margin, continuity also gives a
small neighbourhood of each actual reference on which the raw
terminal gap persists. The established terminal right-half reduction
then applies there, including its endpoint and ordinary-colour
derivatives. It does not follow that every subsequent integration
target satisfies the coupling equations (2): those equations hold
at the critical reference. Wider horizontal variations still require
a comparison on their own domain, and arbitrary height attenuation
still has to be controlled.

This reduces one missing source estimate to exact neighbouring
equations and a specified boundary inequality. It does not prove
that inequality, the global open-source theorem, or the finite-
exception theorem for arbitrary templates.
