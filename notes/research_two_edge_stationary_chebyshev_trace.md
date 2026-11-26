# A Chebyshev trace identity for the original two-edge stationary equation

Private algebraic phase lemma, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or frozen-source edit
is used.

The original stationary equation with one complete outside end has
a polynomial and an \(SL_2\) trace form for every positive integer
crossing power. These identities retain the zero logarithmic charge
when the original local branch is specified. They do not select that
branch from the polynomial alone.

## 1. Original phase and exact elimination

Fix a positive integer \(n\). Use the calibrated edge derivative
\[
 \psi_t(t,u)=-\pi^{-1}
        \operatorname{arsinh}\{\tan(t/2)\cos(u/2)\}
 \tag{1}
\]
of [the original edge phase](research_bare_kernel_thin_rectangle.md),
and the two-edge phase
\[
 \Phi_n(t,u)=\psi(0,t)+\psi(t,u)+\frac{int^2}{4\pi}-it.
 \tag{2}
\]
For \(n\ge3\), the original finite-source comparison with (2) is recorded in
[the degree-two theorem, equation (27)](research_all_nonzero_degree_two_fillings.md).
The following algebra applies for every positive \(n\);
it does not assert a nondegenerate finite saddle for every \(n\).

Put
\[
 z=t/2,\quad c=\cos z,\quad C=\cos(u/2),\quad T=\tan z,
 \qquad A=\operatorname{arsinh}T,\quad B=\operatorname{arsinh}(CT).
 \tag{3}
\]
Work on a chosen holomorphic branch on which
\[
 \sin z\ne0,\quad\cos z\ne0,\quad
 \sinh A=T,\quad\cosh A=\sec z,\quad\sinh B=CT .
 \tag{4}
\]
The equality \(\cosh A=\sec z\) is the calibrated sign of the
original inverse hyperbolic sine, not merely its squared identity.
It holds on the original regular germ and persists under
continuation while these branches and denominators stay regular.

The original zero-charge stationary equation is
\[
                 A+B=i(nz-\pi).
 \tag{5}
\]
Let \(T_n,U_{n-1}\) be the ordinary Chebyshev polynomials, normalized
by
\[
 T_n(\cos z)=\cos(nz),\qquad
 U_{n-1}(\cos z)=\frac{\sin(nz)}{\sin z}.
\]
Define
\[
                 \mathscr P_n(c)=T_n(c)-iU_{n-1}(c).
 \tag{6}
\]

**Lemma 1.** Equation (5), under (4), implies
\[
                         \mathscr P_n(c)=C.
 \tag{7}
\]
More precisely, if \(D=i(nz-\pi)-A\), then the exact identity
\[
 \boxed{\quad
       \sinh D-CT=T\{\mathscr P_n(c)-C\}
       \quad} \tag{8}
\]
holds before imposing stationarity.

*Proof.* The hyperbolic subtraction formula and (4) give
\[
 \sinh D
   =\cos(nz)\tan z-i\sin(nz)\sec z .
\]
Divide by \(T=\tan z\), which is nonzero by (4), and use
the two Chebyshev identities. This proves (8). At a critical
point \(D=B\), so its left side is zero. \(\square\)

For \(n=3\),
\[
 \mathscr P_3(c)=4c^3-3c-i(4c^2-1).
\]
With \(v=2c\), equation (7) is exactly
\[
                  v^3-2iv^2-3v+2i-2C=0
\]
from [the adopted cubic continuation](research_mixed_next_inner_three_cubic_continuation.md).
The terminal one-edge equation \(cU_{n-1}(c)=i\) in
[the terminal-power proof](research_terminal_powers_four_through_thirty_one.md)
is a different stationary source and is not substituted here.

## 2. The logarithmic converse and local branch

The converse needs branch information. Suppose the quantities
in (3)--(4) are holomorphic on a connected parameter domain,
\(\cosh B\ne0\) there, and (7) holds identically.
Then (8) gives \(\sinh D=\sinh B\), which algebraically allows
both families
\[
 D=B+2\pi i k,\qquad
 D=-B+(2k+1)\pi i,\qquad k\in\mathbb Z.
 \tag{9}
\]
They cannot intersect when \(\cosh B\ne0\).
If the original equality \(D=B\) holds at one reference point,
continuity fixes that family and its integer on the connected
domain. Therefore \(D=B\) everywhere, and (5) follows with its
original zero charge. Without this calibration, (7) alone does
not choose (5).

In particular, let \((t_0,u_0)\) be a known stationary point
of the original phase (2), satisfying (4),
\(\cosh B_0\ne0\), and
\[
                         \mathscr P_n'(c_0)\ne0.
 \tag{10}
\]
The implicit function theorem gives a unique nearby holomorphic
root \(c(u)\) through \(c_0\) of (7).
Choose the local inverse \(t(u)=2\arccos c(u)\) through \(t_0\);
it exists because \(\sin(t_0/2)\ne0\).
The original \(A,B\) branches then continue on a sufficiently
small neighborhood and retain (4) and \(\cosh B\ne0\).
The calibrated converse proves the original stationary equation
there. This is a local continuation of the specified phase branch,
not a rule for choosing one among all roots of (7).

The algebraic simplicity in (10) is also exactly the relevant
reduced nondegeneracy. Differentiating (8) at a critical point,
at fixed \(u\), yields
\[
 \boxed{\quad
 \Phi_{n,tt}
    =-\frac{\tan z\,\sin z\,\mathscr P_n'(c)}
                         {2\pi\cosh B}.
 \quad} \tag{11}
\]
Indeed the derivative of its left side is
\(\cosh B(in/2-A_t)-CT_t=\pi\cosh B\,\Phi_{n,tt}\),
and \(c_t=-\sin z/2\).
All remaining factors in (11) are nonzero under the stated
conditions. Thus the reduced critical Hessian vanishes exactly
when \(\mathscr P_n'(c)\) vanishes.

The stationary action near the calibrated reference retains
its original additive constant and has derivative
\[
 \frac{d}{du}\operatorname{stat}_t\Phi_n(t,u)
       =-\pi^{-1}\operatorname{arsinh}\{c(u)\tan(u/2)\},
 \tag{12}
\]
whenever this additional edge branch is continued from the
reference without meeting its cuts. Equation (12) does not
supply a new finite-source coefficient.

## 3. The determinant-one trace form

Set
\[
 \mathsf M(c)=
 \begin{pmatrix}2c&-1\\1&0\end{pmatrix},
 \qquad
 \mathsf D=
 \begin{pmatrix}1&-2i\\0&1\end{pmatrix}.
 \tag{13}
\]
Both matrices have determinant one. With \(U_{-1}=0\), the
Chebyshev recurrence gives, for every \(n\ge1\),
\[
 \mathsf M(c)^n=
 \begin{pmatrix}
 U_n(c)&-U_{n-1}(c)\\
 U_{n-1}(c)&-U_{n-2}(c)
 \end{pmatrix}.
 \tag{14}
\]
For \(n=1\) the last entry is \(-U_{-1}=0\); the general
case follows by multiplying once more by \(\mathsf M\).
Since \(U_n-U_{n-2}=2T_n\), one obtains
\[
 \boxed{\qquad
 \frac12\operatorname{tr}\{\mathsf D\mathsf M(c)^n\}
           =T_n(c)-iU_{n-1}(c)=\mathscr P_n(c).
 \qquad} \tag{15}
\]
Thus the polynomial stationary equation is exactly the
determinant-one trace relation
\[
          \operatorname{tr}\{\mathsf D\mathsf M(c)^n\}
                    =2\cos(u/2).
 \tag{16}
\]
Its characteristic polynomial is
\[
              \lambda^2-2\cos(u/2)\lambda+1,
\]
so its eigenvalues, counted with algebraic multiplicity, are
\(e^{iu/2},e^{-iu/2}\). At a repeated value this makes no
diagonalizability assertion. This is the precise algebraic
Floquet form of (7); the logarithmic converse still requires
Section 2.

No matrix in (13) is asserted here to be an original quantum
crossing operator or a marked gluing representation. No
global selected-root domain for arbitrary \(n\), contour
intersection number, dominant action, finite-kernel packet,
or short-composition theorem follows solely from (15).
The explicit global \(n=3\) guards remain the separate
adopted cubic theorem; its unresolved finite-source
obligations are unchanged.

