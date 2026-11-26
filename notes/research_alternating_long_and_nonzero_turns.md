# Alternating long turns and arbitrary nonzero turns

The finite collection theorem permits any prescribed finite set of
short powers. A two-stage argument can remove that prescribed set.
The extra step is to show that a sufficiently long ordinary turn
restores the constants of the original bare-edge class, even when
its input is controlled only on a smaller disk.

The reset lemma below proves this restoration on the specified fixed
output disk. It gives one threshold for long turns separated by
arbitrary nonzero powers. No assertion about arbitrary adjacent short
powers follows from it.

## 1. Two classes of boundary functions

Use the original operators \(R,T\), the full edge kernel \(K_N\),
and the exact Frobenius trace \(\phi_N\). A controlled class consists
of separately specified constants
\[
                 \rho,H,a,c,C,h>0
\]
and canonical polynomials of spectral degree at most \(N-1\) with
\[
 F_N(u)=\epsilon_N A(u)e^{NW(u)}(1+O_F(N^{-1})),
 \qquad |\epsilon_N|=1,\quad A(u)\ne0,
 \tag{1}
\]
on a neighborhood of \(|u|\le2\rho\), where \(W,A\) are even
holomorphic functions,
\[
 |W(u)-W(0)|\le H,\qquad -\Re W''(u)\ge a>0,
 \tag{2}
\]
and
\[
 |F_N(x+iy)|\le C_FN^{d_F}
       e^{N\{\Re W(0)-c(1-\cos x)+Cy^2\}}
 \quad(|x|\le\pi,\ |y|\le h).
 \tag{3}
\]
The remainder in (1) is holomorphic. Prefactors, remainder constants,
and starting levels may depend on the member. They are not part of
the common class data.

Fix once the bare-edge class \(\mathscr S\) constructed in Section 2
of [the fixed-domain theorem](research_fixed_domain_long_power_turns.md),
choosing its bounds with strict reserve around the bare-edge output
bounds: a larger normalized phase bound, a smaller curvature and
real angular coefficient, and weaker vertical-growth and strip data.
These choices are made now, before either class below or either
threshold depending on it is introduced.
Its disk radius is denoted \(R\), and its other constants by
\(H_S,a_S,c_S,C_S,h_S\). That construction includes every terminal
\(T(R^a)\), \(|a|\ge2\). There is an integer \(B_0\ge2\) such that
\[
          F\in\mathscr S,\quad |b|\ge B_0
          \quad\Longrightarrow\quad T(R^bF)\in\mathscr S.
 \tag{4}
\]
Its constants were chosen to include the bare-edge output bounds,
not just the input terminal bounds. In particular \(a_S\) is at most
the bare-edge joint curvature lower bound, \(H_S\) includes
\(2R^2\sup|\psi_u(t,u)/u|\), and its real angular and strip constants
include the output constants of that theorem.

## 2. A long ordinary turn restores this fixed class

**Reset lemma.** Let \(\mathscr C\) be a controlled class as in
(1)--(3), with any fixed positive constants. There is a finite
threshold \(B_{\rm reset}(\mathscr C,\mathscr S)\) such that
\[
      F\in\mathscr C,\quad |n|\ge B_{\rm reset}
      \quad\Longrightarrow\quad T(R^nF)\in\mathscr S.
 \tag{5}
\]
The target disk is the fixed disk of \(\mathscr S\); it need not be
smaller than the input disk.

**Proof.** Restrict the input disk if necessary, so that
\(\rho\le R\). Choose a real trace cutoff
\[
        0<r<\min(\rho/2,r_w/2),
\]
where \(r_w\) is the full central-kernel radius in Lemma 2 of the
fixed-domain theorem. On \(|t|\le\rho,\ |u|\le2R\), put
\[
             \Phi(t,u)=W(t)+\psi(t,u).
\]
Cauchy's inequality bounds \(W''\) in terms of \(H,\rho\), and the
bare kernel is defined on the entire displayed rectangle. Hence
\[
 |\Phi_{tt}|\le L,\qquad \Re\Phi_{tt}\le-a
 \tag{6}
\]
with one finite \(L\) for the input class. Separate evenness gives
\(\Phi_t(0,u)=0\).

The contraction argument in Section 3 of the fixed-domain theorem
therefore solves
\[
        \Phi_t(t,u)+\frac{in}{2\pi}t=i\lambda
        \qquad(0\le\lambda\le1,\ |u|\le2R)
 \tag{7}
\]
on a disk \(|t|\le C_1/|n|\), for all sufficiently large \(|n|\).
The constants use the input radius \(\rho\) and the output radius
\(R\) separately. More explicitly, take
\[
 C_h=8\pi^2L,\qquad
 \delta=\min(\gamma_e,c_e)(1-\cos(r/2)),
 \tag{7a}
\]
where \(\gamma_e\) is the centered bare-edge constant. It suffices
to increase the threshold until
\[
 |n|>8\pi L,\quad |n|>16\pi/r,\quad
 \frac{C_h}{2n^2}<\min(\delta/4,ar^2/8),\quad
 \frac{C_h}{n^2}<r/4.
 \tag{7b}
\]
The resulting whole charge path satisfies
\[
 |t_\lambda|\le4\pi\lambda/|n|<r/4,\qquad
 \frac{2\pi^2a\lambda}{n^2}
 <-\Im t_\lambda<\frac{C_h\lambda}{n^2}
 \quad(\lambda>0).
 \tag{7c}
\]
Choose the real midpoint cutoff \(a_N\ge r\), with
\(a_N=r+O(N^{-1})\). The entire central trace rectangle then lies
in \(|t|<\min(\rho,r_w)\) for sufficiently large \(N\). These
choices do not require the output radius \(R\) to decrease.

The exact finite trace proof now applies on that rectangle. Its
outer real-node estimate is centered at
\(\Re[W(0)+\psi(0,u)]\), uniformly for \(|u|\le2R\), by the
centered bare-edge estimate. The input's angular loss and first
normal bounds are supplied by (3). The outer gap depends on \(r\)
and the input constants but is strictly positive. Increasing
\(|n|\) makes the selected-action decrease smaller than this gap.
The horizontal contour, its two endpoint currents and its entire
rational charge factor are handled exactly as in the fixed-domain
proof. No expansion of the input is used outside its own disk.

The result is a full nonzero expansion on \(|u|\le2R\), of order
\(N^0\), with phase
\[
 S(u)=W(t_*(u))+\psi(t_*(u),u)
            +\frac{in}{4\pi}t_*(u)^2-it_*(u).
 \tag{8}
\]
The exact unit is \(\epsilon_NC_{N,n}\), where
\(C_{N,n}=\exp(\pi in(N-1)^2/(4N))\), and its amplitude is
\[
 A_{\rm out}(u)=i\sqrt{\frac2\pi}\,
 \frac{\sin t_*(u)\,A(t_*(u))\,a_e(t_*(u),u)}
 {\sqrt{-W''(t_*(u))-\psi_{tt}(t_*(u),u)-in/(2\pi)}}.
 \tag{8a}
\]
The square root is the continued Gaussian branch used in the
original trace theorem. The \(N^0\) power is unchanged:
\(N^2\) from the trace, \(N^{-3/2}\) from the full edge and
\(N^{-1/2}\) from the Gaussian multiply to \(1\).
The input amplitude is evaluated inside its zero-free disk. The
edge amplitude, \(\sin t_*\), and the Gaussian determinant are
nonzero there. The root cannot be \(t_*=0\), since the right side
of (7) at \(\lambda=1\) is \(i\).

The output constants come from the bare kernel. The envelope identity
\[
                    S'(u)=\psi_u(t_*(u),u)
 \tag{9}
\]
gives
\[
 |S(u)-S(0)|\le\frac{L_u}{2}|u|^2
                   \le2L_uR^2<H_S
 \tag{9a}
\]
on the whole target disk, where \(L_u\) is the original fixed
bare-edge bound. The strict inequality is one of the initial
reserve choices; it is not obtained by increasing an input-class
constant.
The Hermitian part of
\[
 -\begin{pmatrix}
 W''+\psi_{tt}+in/(2\pi)&\psi_{tu}\\
 \psi_{ut}&\psi_{uu}
 \end{pmatrix}
\]
is bounded below by the bare-edge joint curvature bound times
the identity, plus \(\operatorname{diag}(a,0)\).
Its Schur complement therefore has real part at least that
bare-edge bound, which is at least \(a_S\). Thus
\(-\Re S''\ge a_S\), regardless of the smaller input value \(a\).

For arbitrary real \(u\), the full central kernel supplies the
output loss \(\gamma_w(1-\cos u)\). The outer-node estimate supplies
the bare-edge loss \(c_e(1-\cos u)\), with an independent strict
gap in the trace variable. Consequently the real output coefficient
is \(\min(c_e,\gamma_w)\), as in the fixed-domain proof; it does
not shrink with the input loss \(c\). The target local phase bounds
and this real angular bound give \(c_S,C_S,h_S\) by the same
polynomial strip continuation. These target constants were fixed
when \(\mathscr S\) was chosen. The input constants affect only
the required threshold and member-dependent prefactors.
This proves (5). \(\square\)

## 3. Removing the finite alphabet

Take the finite set
\[
                \mathcal B_0=\{b\in\mathbb Z:0<|b|<B_0\}.
 \tag{10}
\]
Every two-boundary kernel \(P_{b,N}\), \(b\in\mathcal B_0\), is
covered by
[the all-power degree-two theorem](research_all_nonzero_degree_two_fillings.md).
Apply [the finite collection theorem](research_finite_two_boundary_kernel_closure.md)
to these kernels and the bare edge. Its class \(\mathscr C\) can
be chosen to contain \(\mathscr S\): decrease its disk, curvature,
angular loss and strip width, and increase its normalized phase and
vertical-growth bounds as necessary. The class construction chooses
these constants before its long-power threshold, so this inclusion
does not change that order of choices.

There is consequently a finite \(B_{\rm lib}\) such that
\[
 F\in\mathscr C,\quad b\in\mathcal B_0,\quad |n|\ge B_{\rm lib}
 \quad\Longrightarrow\quad
       T\bigl(R^bT(R^nF)\bigr)\in\mathscr C.
 \tag{11}
\]
Set \(B=\max(B_{\rm lib},B_{\rm reset})\). For \(|n|\ge B\) and
an arbitrary nonzero integer \(b\), there are two cases.
If \(0<|b|<B_0\), use (11).
If \(|b|\ge B_0\), the first turn maps \(\mathscr C\) into
\(\mathscr S\) by (5), and the second preserves \(\mathscr S\)
by (4). Since \(\mathscr S\subset\mathscr C\), in either case
\[
           T\bigl(R^bT(R^nF)\bigr)\in\mathscr C.
 \tag{12}
\]
All thresholds were fixed before this arbitrary \(b\) was chosen.
In particular there is no equation of the circular form
\(B\ge B_*(\{b:|b|<B\})\).

Starting from any terminal \(F_0=T(R^a)\), \(|a|\ge2\), it follows
that every fixed sequence
\[
 F_j=T\bigl(R^{b_j}T(R^{n_j}F_{j-1})\bigr),
 \qquad b_j\ne0,\quad |n_j|\ge B,
 \tag{13}
\]
has a full nonzero boundary expansion and the same class constants.
The threshold is independent of the number of stages and of all
the nonzero integers \(b_j\). Each entire word remains fixed before
\(N\to\infty\).

## 4. Markings, closure, and the limitation

For the finite powers in (10), use the original isolated pieces
with their full primitive periods. This includes the direct
[unit-power geometric comparison](research_degree_two_unit_power_geometry.md).
Choose the common input disk inside the marked geometric charts
of this finite kernel family and the terminal seeds. The geometric
claim concerns the actual members generated by the following
operations; analytic membership in \(\mathscr C\) alone would not
assert that an arbitrary function represents a geometric tangle.
For the other powers, use the original two long turns in (4)--(5).
The charge paths in (7) remain in the input and bare-edge charts;
the larger output disk requires no larger input deformation.
Thus the marked geometric composition and its absolute real
volume anchor are the ones already proved for these two operations.

A sufficiently long fixed final scalar closure of a source in
\(\mathscr C\) has a nonzero \(N^{3/2}\) asymptotic. Under the
original endpoint, parity and no-internal-component conditions
giving a knot, its rate is the hyperbolic volume of that knot's
complement. One final threshold works for the class. As throughout,
all integer powers are fixed before the quantum level tends to
infinity.

The restriction \(b_j\ne0\) has content. At zero,
\(T(R^0T(R^nF))=R^nF\), and an arbitrarily large boundary chirp
does not obey a fixed normalized phase bound. Zero vertices can
also merge neighboring powers with cancellation. Those assignments
must be tracked separately; they cannot be declared finitely many.
Likewise (13) leaves out arbitrary consecutive short nonzero
powers. The result enlarges the uniform composition class but is not
the finite-exception theorem.
