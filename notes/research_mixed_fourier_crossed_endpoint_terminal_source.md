# The first crossed Fourier endpoint is an original terminal value

Research deduction, 7 November 2026. The endpoint coefficient generated
by one actual crossing is exactly a known whole ordinary terminal
polynomial at its first physical color. That color tends to \(+2\),
not to the complete color \(-2\). This identifies the source without
continuing a complex-output asymptotic to the unit circle. Existing
real-color upper envelopes apply with their stated domains; comparison
with the action of a crossed source remains separate.

No numerical evaluation or new source comparison is used.

## 1. Exact identification, including every scalar

Use \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\),
\(r=q^{-2}\), \(P_j=(r;r)_j\), and
\(\kappa=q^{D^2/2}\). The notation \(c_0=q+q^{-1}\) below
denotes an ordinary color, not a Fourier coefficient.
Let
\[
 \begin{split}
 X&=e^{-2\pi ia},\qquad
 Z_N(a,y)=\sum_{l=0}^{N-1}C_{1,N}(X,r^l)f_l(y),\\
 f(y)&=S h(y),\qquad
 S=\operatorname{diag}\!\left(
                 \frac{\kappa^{-1}(-q)^{-l}}{P_l}\right)M,\\
 \mathbf b(w)&=S v(w),\qquad v(w)=(e_0(w),\ldots,e_D(w))^T .
 \end{split}
 \tag{1}
\]
These are the original bases and crossing in
[exact wire contraction](research_mixed_wire_exact_contraction.md),
equations (6), (13)--(14).
The whole type-four terminal identity in
[the ordinary-color transform](research_mixed_terminal_color_transform.md),
equations (6)--(7), is
\[
 \mathcal V_{1,N}(w,X)
       =\sum_{l=0}^{N-1}C_{1,N}(X,r^l)b_l(w).
 \tag{2}
\]
In particular it has no additional scalar \(N\) or \(\kappa\).
The equivalent whole three-index source, with all Newton data,
is given in
[the joint terminal source](research_mixed_terminal_four_joint_source.md),
equations (2)--(4).

**Proposition 1.** At every level and both parities,
\[
 \boxed{\quad
 Z_N(a,0)=\mathcal V_{1,N}(c_0,X)
            =\sum_{l=0}^{N-1}\frac{C_{1,N}(X,r^l)}{P_l},
       \qquad c_0=2\cos(\pi/N).
 \quad}
 \tag{3}
\]
Consequently the exact first-crossing projection is
\[
       \Pi_0\mathcal M_1 Z_N(a,y)
             =\kappa f_0(y)\mathcal V_{1,N}(c_0,X).
 \tag{4}
\]

*Proof.* The original Newton product \(e_l(w)\) contains
\(c_0-w\) whenever \(l\ge1\), while \(e_0=1\).
Thus \(v(c_0)=\mathbf e_0\). The cardinal identity gives
\(h(0)=\mathbf e_0\), at even as well as odd levels.
It follows that \(\mathbf b(c_0)=S\mathbf e_0=f(0)\).
The finite polynomial formula for \(f_l\) and \(P_D=N\) give
\[
 f_l(0)=\frac1N\prod_{k=l+1}^{D}(1-r^k)=\frac1{P_l}.
 \tag{5}
\]
Substitution into (1)--(2) proves (3).
Equation (4) now follows from the exact identity
\(\Pi_0\mathcal M_1G=\kappa G(0)f_0\) for every Fourier-band
function \(G\), proved in
[the closing interface](research_mixed_fourier_boundary_closing_interface.md),
equations (36)--(37). No evaluation functional is replaced by
an eigenvector at an arbitrary ordinary color. \(\square\)

This specializes the original polynomial to one physical value.
It does not delete its ordinary normal data before forming
that polynomial, nor assert a first-normal estimate at \(c_0\).

There is also an exact unit-circle Wall expression. Set
\(\rho_j(X)=X^{-j}(rX;r)_j\), and retain the finite polynomial
\[
 W_{n,N}(u;a)=\sum_{l=0}^{n}
        \frac{(r^{-n};r)_l\,u^l}{P_l(ar;r)_l},
                    \qquad 0\le n<N .
 \tag{6}
\]
Expanding only the literal conditional sum in (3) gives
\[
 \begin{split}
 Z_N(a,0)
   &=\sum_{j+l<N}
           \frac{\rho_j(X)P_{j+l}}{P_j^3P_l^2}\\
   &=\sum_{j=0}^{N-1}\frac{\rho_j(X)}{P_j^2}
                         W_{N-j-1,N}(1;1).
 \end{split}
 \tag{7}
\]
Indeed \(P_{j+l}=P_j(r^{j+1};r)_l\) and
\(r^{-(N-j-1)}=r^{j+1}\). All denominators in (6)--(7)
have indices below \(N\), so the specialization \(a=u=1\)
is finite and regular. The support wall in (7) is literal.
The initialized complex-\(Y\) Wall asymptotic does not cover
this unit-circle parameter and is not used in (3) or (7).

## 2. Exactly which existing bounds transfer

Let \(\mathcal E_1(a)\) be the complete 27-profile upper
envelope of
[the all-real-color terminal profile theorem](research_mixed_terminal_profile_real_color_lift.md),
equation (4). Its Theorem 1 applies to every
\(a\in[.22,.45]+i[-.12,.12]\), independently of ordinary
reference eligibility. Since
\[
 c_0=-2\cos\theta_N,\qquad
           \theta_N=\pi-\pi/N\in[-\pi,\pi],
 \tag{8}
\]
(3) gives, for every prescribed \(\tau>0\),
\[
 |Z_N(a,0)|\le C_\tau N^{A_\tau}
                         e^{N\{\mathcal E_1(a)+\tau\}} .
 \tag{9}
\]
Thus (4) supplies an actual finite-source upper for the new
projection. On any fixed compact output neighborhood with
\(|Y|=|e^{2\pi iy}|<1\),
\[
 |\Pi_0\mathcal M_1 Z_N(a,y)|
     \le C_\tau' N^{A_\tau'}
             e^{N\{\mathcal E_1(a)+\pi\Im y+\tau\}} .
 \tag{10}
\]
Here \(|\kappa|=1\) and the exact identity
\[
 f_0(y)=\frac{e^{-\pi iDy}}N\,\frac{1-Y^N}{1-Y}
 \tag{11}
\]
retains the original cardinal normalization. The factor
\(\pi\Im y\) in (10) is part of the rate, not a polynomial
cost.

The stronger
[real-color decay theorem](research_mixed_terminal_real_color_decay.md),
Theorem 1, additionally requires its original actual ordinary
terminal-reference family. On that family, with
\(a_*=A+iH\), target \(a=x+iH\), and its own ordinary
terminal plane \(B_{1,0}(a_*;x)\), equations (3) and (8) imply
\[
 |Z_N(a,0)|\le C N^A
  e^{N\{B_{1,0}(a_*;x)-c(1+\cos(\pi/N))\}},\qquad c>0.
 \tag{12}
\]
The corresponding unselected incoming halfweight retains
exactly the allocation in equation (3) of that theorem.
The coefficient in (12) has a uniform positive angular loss,
because the chosen colors approach \(+2\): its displayed loss
is \(c(1+\cos(\pi/N))\ge c\), tending to \(2c\).
More precisely, equation (16) in the proof of that theorem
retains separate positive constants \(c_{\rm reg}\) and
\(\gamma_{\rm rest}\) for the regular densities and the
restored physical sectors. Its strongest immediate combined
loss at this angle is
\[
 \delta_N=\min\{c_{\rm reg}(1+\cos(\pi/N)),
                                      \gamma_{\rm rest}\}
       \longrightarrow
       \min\{2c_{\rm reg},\gamma_{\rm rest}\}.
 \tag{13}
\]
Replacing the loss in (12) by \(\delta_N\) only changes its
polynomial prefactor. These constants are those supplied by
the existing theorem, not newly evaluated numbers.
The unrestricted profile bound (9) does not supply the same
strict angular loss relative to \(\mathcal E_1\): some of its
physical profiles were retained only with a no-loss color bound.

Equation (12) is not automatically a claim at every independent
Fourier-ended reference. In particular, an incoming type-four
point must satisfy the ordinary terminal source's oriented and
inverse-leg conditions relative to its ordinary endpoint map;
membership in a reduced disk alone does not prove those
conditions. This distinction is explicit in
[canonical source eligibility](research_mixed_terminal_canonical_source_domain.md),
Sections 2--3. Even when that eligibility is proved, the
ordinary terminal action defining \(B_{1,0}\) has not here
been identified with the action of \(\mathcal M_1Z_N\).

## 3. Type-three incoming references require no additional filter

There is one immediate actual Fourier-reference subcase.
Retain the typed domain
\[
 \begin{split}
 D_3&=\{|a-(.35-.01i)|\le.09\},\\
 K_3&=\{|a-(.35-.01i)|\le.083\}
   \cap\{-.072\le\Im a\le.068,\ \Re a-3\Im a\le.608\}.
 \end{split}
 \tag{14}
\]
These are the original domains in
[canonical source eligibility](research_mixed_terminal_canonical_source_domain.md),
equations (1)--(2).

**Proposition 2.** For every \(a_*=A+iH\in K_3\), use the
original own-four ordinary endpoint map at \(a_*\) to define
\(\mathcal P_1(a_*)\) and \(B_{1,0}(a_*;x)\).
Then (12)--(13) hold uniformly for \(a=x+iH\), \(x\in[.22,.45]\).
This includes actual Fourier-ended incoming legs of type three.
It does not assert that each point of \(K_3\) is realized by an
ordinary-ended word.

*Proof.* The completed terminal-four source certificate has no
coupled or oriented restriction on its type-three input disk.
[The oriented continuation](research_mixed_terminal_four_oriented_source_continuation.md),
Section 1, keeps the full \(D_3\).
[The coupled continuation](research_mixed_terminal_four_coupled_source_continuation.md),
Sections 1 and 3, explicitly forbids its added inverse-leg
exclusions on every type-three input. The complete source and replay
in [the unselected plateau theorem](research_mixed_full_unselected_plateau.md),
Section 1, therefore establish all twenty-one original comparisons
on \(D_3\), not merely at known finite-word realizations there.

The other hypotheses in the complete source partition also hold
on \(K_3\). Indeed
\[
 .267\le A\le.433,\qquad -.072\le H\le.068.
 \tag{15}
\]
The original endpoint map is already defined on all of \(D_3\).
Its own-four attached output satisfies
\(.246<\Re t_*<.350\) and
\(-.108<\Im t_*<-.020\); its private output satisfies
\(.333<\Re e_*<.363\) and
\(-.051<\Im e_*<-.019\).
These are the full-map bounds in
[terminal source reduction](research_mixed_terminal_conditional_source_reduction.md),
Section 1, rather than estimates requiring a particular word.
They place the private output strictly inside the original
coherent endpoint rectangle.

For the coherent physical end rows,
[the terminal end-tail proof](research_mixed_terminal_transform_tails.md),
Section 2, proves its reference action floor on the entire
disk \(D_3\); its reference slope proof uses precisely
\(.24\le A\le.433\), \(|H|<.12\), and these full-map
attached-output bounds. Thus its original supporting-plane
gap remains valid on (14).
The left-transform and private-tail proofs use only the target
tube \([.22,.45]+i[-.12,.12]\), the whole endpoint coefficient,
and their original physical support. The remaining raw upper
triangle is one of the completed twenty-one comparisons.
No additional adjacent-ordinary inverse condition occurs in
any of these arguments for a type-three input.

Consequently the unchanged complete partition in
[whole terminal-four completion](research_mixed_terminal_four_full_completion.md),
Section 2, applies at every reference (14).
The proof of real-color decay then retains exactly its regular
angular loss and its strictly paid restored sectors, giving
(12)--(13). Compactness of \(K_3\), its strict inclusion in
\(D_3\), the original compact endpoint images, and the finite
collection of source families give common constants. \(\square\)

For incoming type four, the corresponding conclusion is not
obtained merely from the actual Fourier input being in \(K_4\).
The ordinary terminal map \(E_4(a_*)\) used in its inverse-leg
conditions is different from the attached solution of the
Fourier-ended last block. The latter's equations do not
automatically verify the former's conditions.

The new exact observation is therefore a known original terminal
polynomial, with the valid whole-source bounds (9)--(10) and
the calibrated consequence (12) on its eligible domains, now
including all of (14). An exponential
gap relative to the crossed source still requires its calibrated
action comparison and nonzero local coefficient. This note proves
neither such a gap nor its failure, and makes no arbitrary
short-filling or knot-family conclusion.
