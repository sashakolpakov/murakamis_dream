# The common original Jacobi characteristic of the triple-row pressure

Private written proof, 17 November 2026.

The critical equations of the positive triple-row pressure reduce
to one strictly monotone scalar equation. Its selected solution is
the common characteristic of the original Jacobi operators, and
it computes the leading coefficient of every fixed-degree
polynomial inserted in the original closing trace.

The source equations hold exactly, with their original forcing
canceled by the full trace ideal. The characteristic and
fixed-degree observations are asymptotic statements on strict
physical support. They do not supply a stable continuation of
external first normals or a lower bound after a crossing whose
canonical polynomial degree grows with the level.

## 1. Original source and exact coupled equations

Set
\[
 N\ge2,\quad D=N-1,\quad \eta=(-1)^D,\quad
 s_r=2\sin(\pi r/N),\quad S_r=\prod_{a=1}^rs_a,
\]
\[
 c_r=2\cos((2r+1)\pi/N),\quad
 e_r(C)=S_r^{-2}\prod_{a<r}(c_a-C),\quad
 P_N(C)=2T_N(C/2)+2,
\]
\[
 \phi(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f,\qquad
 K_N(w,C)=\sum_{r=0}^De_r(w)e_r(C),\qquad
 F_j(C)=K_N(c_j,C).
 \tag{1}
\]
Physical indices satisfy \(0\le j\le\lfloor D/2\rfloor\).
The quotient and trace in (1) retain the double-node first
normals and the odd simple node.

For a polynomial \(q\), define the ordinary external polynomial
\[
 \Gamma_{q,N}(\mathbf w)
       =\phi_C\!\left(q(C)\prod_{i=1}^3K_N(w_i,C)\right),
 \qquad \Gamma_N=\Gamma_{1,N}.
 \tag{2}
\]
Only the class of \(q\) modulo \(P_N\) enters this expression.

Write \(\mathscr J_N\) for the original ordinary operator.
On the angular lift \(C_N(x)=2\cos(2\pi x+\pi/N)\), it is
\[
 \mathscr J_N f=(c_0+A_N+B_N)f
                  -A_Nf(x+N^{-1})-B_Nf(x-N^{-1}),
\]
\[
 A_N(x)=\frac{s_{Nx+1}^4}{s_{2Nx+1}s_{2Nx+2}},
 \qquad
 B_N(x)=\frac{s_{Nx}^4}{s_{2Nx}s_{2Nx+1}}.
 \tag{3}
\]
Its ordinary polynomial action and kernel source are
\[
 \mathscr J_Ne_r=c_re_r-s_r^2e_{r-1},\qquad
 (C-\mathscr J_{N,w})K_N(w,C)
    =\frac{P_N(C)P_N(w)}{N^4(w-c_0)}.
 \tag{4}
\]
The last fraction in \(w\) is a polynomial. The convention
\(e_{-1}=0\) is used in the first identity.

Multiply the second identity by the other two kernels and
by \(q(C)\), and apply the original trace in \(C\).
Its right side is divisible by the full \(P_N(C)\), so
it vanishes with all multiplicities. Consequently
\[
 \boxed{\qquad
 \mathscr J_{N,w_i}\Gamma_{q,N}
                  =\Gamma_{Cq,N}\quad(i=1,2,3).
 \qquad}
 \tag{5}
\]
In particular
\[
 (\mathscr J_{N,w_i}-\mathscr J_{N,w_k})\Gamma_{q,N}=0,
 \qquad
 q(\mathscr J_{N,w_i})\Gamma_N=\Gamma_{q,N}.
 \tag{6}
\]
These are ordinary polynomial identities in the external
variables, not equalities only at distinct physical values.
They therefore retain every external derivative as well.
The cancellation in (5) occurs under the original closed
\(C\)-trace; no forcing has been deleted from a free kernel.

At a regular physical bulk index, (5) reads
\[
 \begin{split}
 &(c_0+A_j+B_j)\Gamma_{\mathbf j}
       -A_j\Gamma_{\mathbf j+\mathbf e_i}
       -B_j\Gamma_{\mathbf j-\mathbf e_i}\\
 &\hspace{35mm}
       =\phi\!\left(CF_{j_1}F_{j_2}F_{j_3}\right),
 \end{split}
 \tag{7}
\]
where \(j=j_i,\ A_j=A_N(j/N),\ B_j=B_N(j/N)\).
The right side is the same for every \(i\).

## 2. One scalar equation selects the pressure branch

Let
\[
 \mathcal X^\circ
       =\{\mathbf x:0<x_i<1/2,\ \sum_i x_i>1\}.
 \tag{8}
\]
Here \(x_i\) is a macroscopic degree fraction. The exact
finite physical color remains \(c_{j_i}\) in (1).
Use the pressure action from the first direct source:
\[
 \mathcal J(u)=\int_0^u\log(2\sin\pi v)\,dv,
 \qquad
 f(x,t)=\mathcal J(x+t)-\mathcal J(x-t)-2\mathcal J(t),
\]
\[
 \Phi(\mathbf x,\mathbf t)=
   \sum_i f(x_i,t_i)
   +\sum_{i<k}\mathcal J(t_i+t_k)-\sum_i\mathcal J(t_i)
   -\mathcal J(t_1+t_2+t_3-1).
 \tag{9}
\]
Its unique maximum has
\(0<t_i^*<x_i,\ \sum_i t_i^*>1\), and
\(\mathcal G(\mathbf x)=\Phi(\mathbf x,\mathbf t^*)\).
The Hessian in the internal variables is negative definite.

Introduce different letters for their cotangents:
\[
 X_i=\cot(\pi x_i)>0,\qquad
 Y_i=\cot(\pi t_i^*)>X_i,\qquad
 S=\sum_{i<k}Y_iY_k.
 \tag{10}
\]
Since \(\sum_i t_i^*\in(1,3/2)\),
\[
 \sin\!\left(\pi\sum_i t_i^*\right)
       =\left(\prod_i\sin\pi t_i^*\right)(S-1)<0.
 \tag{11}
\]
Thus \(S<1\). The same identity for the \(x_i\) gives
\(\sum_{i<k}X_iX_k<1\).

The stationary equation in \(t_i\) is
\[
 \frac{\sin\pi(x_i+t_i)\sin\pi(x_i-t_i)
       \sin\pi(t_i+t_j)\sin\pi(t_i+t_k)}
      {\sin^3\pi t_i\,
                   \sin\pi(t_1+t_2+t_3-1)}=1.
 \tag{12}
\]
All factors are positive on the selected real domain.
In cotangents this becomes
\[
 (Y_i^2-X_i^2)(Y_i+Y_j)(Y_i+Y_k)
                         =(1+X_i^2)(1-S).
 \tag{13}
\]
The elementary identity
\((Y_i+Y_j)(Y_i+Y_k)=Y_i^2+S\) makes (13) much simpler:
subtracting its right side and factoring gives
\[
       (1+Y_i^2)\{Y_i^2-X_i^2-(1-S)\}=0.
 \tag{14}
\]
Hence all three differences are equal.

**Theorem 1.** The selected critical point is exactly
\[
 Y_i=\sqrt{X_i^2+L},\qquad
 t_i^*=\pi^{-1}\operatorname{arccot}\sqrt{X_i^2+L},
 \tag{15}
\]
where \(L>0\) is the unique solution of
\[
 E(L,\mathbf X):=
 L+\sum_{i<k}\sqrt{X_i^2+L}\sqrt{X_k^2+L}-1=0.
 \tag{16}
\]
It satisfies
\[
 0<L\le
       \frac{1-\sum_{i<k}X_iX_k}{4}\le\frac14,
 \qquad
 E_L=1+\frac12\sum_{i<k}
                    \left(\frac{Y_i}{Y_k}+\frac{Y_k}{Y_i}\right)
                   \ge4.
 \tag{17}
\]
The branch is real analytic on (8), uniformly nondegenerate
on its compact subsets, and has a single compatible
holomorphic germ near each such real point.

**Proof.** The critical point just proved to exist satisfies
(15)--(16), by (14). Conversely \(E(0,\mathbf X)<0\);
the derivative in (17) is at least four and \(E\) tends
to infinity. This proves unique existence and the upper
bound in (17). For its solution \(Y_i>X_i>0\) and
\(S=1-L<1\). Therefore \(0<t_i<x_i<1/2\), and
(11) implies \(\sum_i t_i>1\). Thus (12) holds on the
original feasible domain, and this is the pressure
maximizer. Positivity of the square roots and \(E_L\ne0\)
give the analytic assertions. On a compact subset,
\(L\) and the square roots stay uniformly away from zero,
so the same implicit-function argument has fixed local
complex buffers. \(\square\)

The choice of positive square roots and of the original
real logarithms is part of this branch selection.
Continuation to a distant complex point requires retaining
those branches and avoiding their discriminants; (17) is
not by itself a global complex continuation estimate.

## 3. The action gradient and the actual common source characteristic

The envelope derivative of (9) is
\[
 p_i:=\partial_{x_i}\mathcal G
  =\log\frac{\sin\pi(x_i+t_i^*)}{\sin\pi(x_i-t_i^*)}
  =\log\frac{Y_i+X_i}{Y_i-X_i}
  =2\operatorname{arsinh}\frac{X_i}{\sqrt L}.
 \tag{18}
\]
Every equality uses the selected positive real branch.
Define
\[
                         \zeta(\mathbf x)=2-\frac4{L(\mathbf x)}.
 \tag{19}
\]
At a macroscopic bulk index, the coefficients in (3) obey
\[
 c_0=2+O(N^{-2}),\qquad
 A_j,\ B_j=\tan^2(\pi x_i)+O(N^{-1})
                    =X_i^{-2}+O(N^{-1}).
 \tag{20}
\]
The leading symbol of its physical recurrence is therefore
\[
 2+\frac2{X_i^2}
       -\frac{e^{p_i}+e^{-p_i}}{X_i^2}
   =2-\frac4L=\zeta,
 \tag{21}
\]
independently of \(i\), because
\(\sinh^2(p_i/2)=X_i^2/L\).

This identity is realized by the actual source, not only
by the stationary equations. The pressure theorem gives,
uniformly on every \(K\Subset\mathcal X^\circ\),
\[
 \Gamma_{\mathbf j}
 =N^{-3}\mathcal A(\mathbf j/N)
           e^{N\mathcal G(\mathbf j/N)}(1+O_K(N^{-1})),
                         \qquad \mathcal A>0.
 \tag{22}
\]
Its neighboring physical indices remain in a slightly
larger strict compact for sufficiently large \(N\).
Thus
\[
 \frac{\Gamma_{\mathbf j\pm\mathbf e_i}}{\Gamma_{\mathbf j}}
             =e^{\pm p_i(\mathbf j/N)}(1+O_K(N^{-1})).
 \tag{23}
\]
Substituting into the exact equation (7) proves
\[
 \boxed{\qquad
 \frac{\phi(CF_{j_1}F_{j_2}F_{j_3})}
      {\phi(F_{j_1}F_{j_2}F_{j_3})}
     =\zeta(\mathbf j/N)+O_K(N^{-1}).
 \qquad}
 \tag{24}
\]
The original trace in numerator and denominator includes
all internal first normals.

By (17), \(\zeta\le-14\), with strict inequality on (8).
It lies outside the physical Casimir spectrum
\(\{c_r\}\subset[-2,2]\).
This is an asymptotic characteristic of a growing source
packet and a ratio of an indefinite original observation.
It is not an additional eigenvalue of the finite operator,
nor is (5) being replaced by an exact eigenvector equation.

## 4. Fixed-degree inserted coupons have a calibrated coefficient

**Theorem 2.** Fix an integer \(d\ge0\) and a compact
\(K\Subset\mathcal X^\circ\). For any polynomial
\(q(C)=\sum_{r=0}^dq_rC^r\), uniformly over physical
triples with \(\mathbf j/N\in K\),
\[
 \frac{\phi(q(C)F_{j_1}F_{j_2}F_{j_3})}{\Gamma_{\mathbf j}}
       =q(\zeta(\mathbf j/N))
                    +O_{K,d}\!\left(N^{-1}\sum_{r=0}^d|q_r|\right).
 \tag{25}
\]
The coefficients may depend on \(N\); the displayed
coefficient norm records that dependence. In particular,
if they stay bounded and \(|q(\zeta)|\) has a positive
lower bound on \(K\), uniform in \(N\), this original coupon has the
nonzero leading coefficient \(q(\zeta)\) times (22).

**Proof.** By (6) the numerator is exactly
\(q(\mathscr J_{N,w_1})\Gamma_N\) at the physical triple.
For a fixed \(r\), expand \(r\) successive applications
of the three-term physical recurrence. It involves only
the indices \(j_1-r,\ldots,j_1+r\); they all lie in the
regular bulk for large \(N\). Each coefficient is bounded
uniformly and changes by \(O(N^{-1})\) under these
finitely many shifts. For every fixed integer \(v\),
(22) likewise gives
\[
 \frac{\Gamma_{\mathbf j+v\mathbf e_1}}{\Gamma_{\mathbf j}}
       =e^{v p_1(\mathbf j/N)}(1+O_{K,d}(N^{-1})).
 \tag{26}
\]
Thus the finite recurrence expansion, including all its
signs, is its constant-coefficient symbol to the \(r\)-th
power, with absolute error \(O_{K,d}(N^{-1})\).
By (21) that symbol is \(\zeta\).
Linearity in the coefficients of \(q\) proves (25).
No absolute replacement of the original trace has occurred.
\(\square\)

The number of steps must remain fixed here. A literal
crossing \(R^n\), even for fixed nonzero \(n\), generally
has canonical degree growing with \(N\); it is not
covered by (25). The theorem also does not estimate
external \(G_j\) insertions. Their activated Newton
bands require a separate coherent comparison beyond
the established fold window.

## Complete direct sources

Both complete texts were read and their directly used
implications checked at the following pins:

* [Triple-row pressure](research_physical_triple_row_pressure.md),
  SHA256 df556243507231e0edb2ea5234163b29623b6d5751b9be987d8f4d967170db4e:
  the exact scalar, strict optimizer, its gradient and
  the uniform nonzero physical amplitude.
* [Ordinary Jacobi source and period monodromy](research_unturned_endpoint_exact_period_monodromy.md),
  SHA256 d082d1ef103c7c200340e36c6a79442ee658bf2582549cd399acb0384391a7a1:
  the ordinary triangular operator, its original kernel
  forcing and full characteristic multiplicities.

Only written mathematics, source-text reads and metadata
hashes were used. No mathematical programs, numerical
evaluations, tests, builds or compilations were run.
Frozen notes and public manuscripts were not changed.
