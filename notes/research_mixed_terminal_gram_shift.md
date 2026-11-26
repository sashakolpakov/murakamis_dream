# Exact forced transport for the contracted terminal boundary

Research deduction, 5 November 2026. The fully contracted terminal
polynomial has a finite q-difference relation with an explicit last-row
forcing. At type four this forcing is \(-(X^{-N}-1)/N^2\), for every
ordinary color and both level parities. Its rate is already below the
actual terminal supporting plane. The relation also contains a shifted
cap transform, so it is not yet a closed equation or upper bound for
the terminal polynomial alone.

## 1. The exact matrix source is not a single crossing power

Retain the original matrices \(M,\mathbf J\), scalar
\(\kappa\), Newton evaluation vector \(v(w)\), and change of basis
\(b(w)=Sv(w)\) from the
[exact wire contraction](research_mixed_wire_exact_contraction.md).
Thus
\[
\begin{gathered}
A_n=\mathbf J M^n,\qquad
\Gamma=SS^T,\qquad A_n=S^TB_nS,\\
S=\operatorname{diag}\left(\frac{\kappa^{-1}(-q)^{-a}}{P_a}\right)M,
\qquad M\mathbf J M=\kappa M^*,\\
q=e^{\pi i/N},\qquad r=q^{-2},\qquad P_j=(r;r)_j.
\end{gathered}
\tag{1}
\]
The adjoint identity uses the original
\(M^{-1}=\overline M\) and \(M^T=\mathbf J M\mathbf J\).
Indices \(a,j\) run from zero to \(N-1\).

The [exact terminal contraction](research_mixed_reversed_cap_assembly.md)
gives, for \(n=3+\epsilon\) and \(\epsilon\in\{0,1\}\),
\[
\begin{split}
\mathcal V_{\epsilon,N}(w,r^a)
 &=\frac{P_a}{\kappa^{1+\epsilon}N^\epsilon}
                  (\Gamma B_{3+\epsilon}b(w))_a\\
 &=\frac{(-q)^{-a}}{\kappa^{2+\epsilon}N^\epsilon}
                  (M\mathbf J M^{3+\epsilon}v(w))_a\\
 &=\frac{(-q)^{-a}}{\kappa^{1+\epsilon}N^\epsilon}
                  (M^*M^{2+\epsilon}v(w))_a .
\end{split}
\tag{2}
\]
Indeed \(\Gamma B_n b=SA_nv\), and the two last equalities
follow from (1). The physical values in (2) determine the unique
Laurent polynomial with band \([-N+1,0]\). Color differentiation
commutes with every displayed operation.

In particular type four retains \(M^*M^3v(w)\), together with its
specified outgoing coefficient observation. The
[arbitrary terminal-power formulas](research_terminal_powers_qbinomial.md)
instead evaluate \(\mathsf T(R^n)\), whose coefficient vector starts
from the algebra unit. Their original boundary vector and matrix
word are different. Equation (2) does not identify \(\mathcal V_1\)
with one of those polynomials or import a packet for it.

## 2. A forced q-difference identity for the Gram transform

For a polynomial \(F\), define its exact transform
\[
\begin{split}
\mathscr G_d[F](X)
 &=\sum_{i=0}^{N-1}\frac{F(r^i)}{P_i^d}\rho_i(X),
 \qquad d\in\{1,2\},\\
\rho_i(X)&=X^{-i}(rX;r)_i
             =\prod_{j=1}^i(X^{-1}-r^j),\qquad \rho_0=1.
\end{split}
\tag{3}
\]
Thus \(\mathcal V_{\epsilon,N}=\mathscr G_{1+\epsilon}
[\mathcal U_{\epsilon,N}]\), with the original ordinary-color cap.
Let
\[
(\sigma f)(X)=f(rX),\qquad
K=(1-rX)\sigma+rX,\qquad Zf=X^{-1}f .
\tag{4}
\]
Here \(Z\) denotes multiplication, and the order of operators below
is part of the formula. Direct product identities give
\[
K\rho_i=r^{-i}\rho_i,\qquad
(Z-rK^{-1})\rho_i=\rho_{i+1},\qquad
\rho_N=X^{-N}-1.
\tag{5}
\]
The inverse in (5) is well-defined on the span of
\(\rho_0,\ldots,\rho_N\): every eigenvalue \(r^{-i}\) is nonzero.
No inverse occurs in the final transport identity.

**Proposition 1.** For every polynomial \(F\), at every level \(N\ge2\),
\[
\boxed{\quad
(K-1)^d\mathscr G_d[F(r^{-1}\,\cdot)]
 =(K^dZ-rK^{d-1})\mathscr G_d[F]
       -\frac{F(r^{N-1})}{N^d}(X^{-N}-1).
\quad}
\tag{6}
\]

*Proof.* Applying \(Z-rK^{-1}\) to (3) raises each basis index by
one. Reindexing the first \(N-1\) terms and using
\(P_i=(1-r^i)P_{i-1}\) gives
\[
(Z-rK^{-1})\mathscr G_d[F]
 =(1-K^{-1})^d\mathscr G_d[F(r^{-1}\,\cdot)]
       +\frac{F(r^{N-1})}{N^d}\rho_N .
\]
The coefficient with index zero on the right vanishes exactly.
The last term uses \(P_{N-1}=N\); it is not part of that
vanishing index. Multiply by \(K^d\), noting \(K\rho_N=\rho_N\),
to obtain (6). \(\square\)

For convenience \(KZ=r^{-1}ZK+(r-1)\), so the right operator is
\(r^{-1}ZK-1\) for \(d=1\), and
\(r^{-2}ZK^2-r^{-1}K\) for \(d=2\).
Also \(K-1=(1-rX)(\sigma-1)\). These are exact finite
q-difference operators, not their commuting symbols.

At the last physical outgoing index, the original cap satisfies
\[
\mathcal U_{\epsilon,N}(w,r^{N-1})
 =\mathcal H_N(w,1)=1 .
\tag{7}
\]
All positive private indices vanish in the first equality; all
positive Newton indices vanish in the second. Thus (6) specializes
at type four to
\[
\begin{split}
(K-1)^2\mathscr G_2[\mathcal U_{1,N}(w,r^{-1}\,\cdot)]
={}&(r^{-2}ZK^2-r^{-1}K)\mathcal V_{1,N}(w,X)\\
 &-\frac{X^{-N}-1}{N^2}.
\end{split}
\tag{8}
\]
Every fixed positive ordinary derivative has the differentiated
identity with zero forcing. The complete-color forcing remains at
both parities, even when some other Newton rows vanish.

This is not a closed equation for \(\mathcal V_1\): the left side
contains the cap evaluated at its shifted physical arguments.
Replacing that source by an unshifted homogeneous solution is not
justified by (8).

There is a useful exact degree check. The value
\(\mathcal H_N(w,r^{-j})\) has ordinary degree at most \(j\).
The cap at \(r^i\) retains only \(j\le N-1-i\). Therefore,
viewed as a polynomial in \(w\) and \(Z=X^{-1}\),
\[
\deg_{\rm total}\mathcal V_{\epsilon,N}\le N-1,\qquad
[Z^{N-1}]\mathcal V_{\epsilon,N}=\frac1{N^{1+\epsilon}}.
\tag{9}
\]
Its \(k\)-th ordinary derivative consequently has \(Z\)-degree
at most \(N-1-k\). These are identities of the whole original
boundary polynomial, with no semisimple quotient.

## 3. The explicit forcing already has a geometric reserve

Let \(a_*=A+ic_*\) be an actual external reference of an open terminal
block, \(a=y+ic_*\), \(y\in[.22,.45]\), \(d_a=y-A\), and
\(\kappa_*=1/2500000\). The
[terminal end-tail theorem](research_mixed_terminal_transform_tails.md)
proves, for both terminal types,
\[
\Re\mathcal P_\epsilon(a_*)+
 \Re\mathcal P_\epsilon'(a_*)d_a-\kappa_*d_a^2>89/100 .
\tag{10}
\]
Here \(|c_*|<.12\). For \(X=e^{-2\pi ia}\),
\[
\left|\frac{X^{-N}-1}{N^{1+\epsilon}}\right|
 \le 2N^{-1-\epsilon}
       e^{\,2\pi N(-c_*)_+}
 <2N^{-1-\epsilon}e^{132N/175}.
\tag{11}
\]
Since \(89/100-132/175>1/10\), this forcing has a strict
supporting-plane reserve \(1/10\), uniformly on the entire target
plateau. If the external type is four, multiply by its actual
unselected halfweight: its rate is \(-\Re g(y+ic_*)/2\), and the
same convex supporting-line argument as in the end-tail theorem
adds exactly the allocated reference tangent. No selected-neighbor
scope is inferred.

The factor \(X^{-N}-1\) vanishes at physical \(X\), but cannot be
dropped on deformed circles. It records a boundary term of the
already contracted transform. It is not an additional Fourier
alternative to be counted a second time. Inequality (11) bounds
this forcing only; it supplies no stability estimate for solving
(8) and no bound for its shifted-cap term.

## 4. Where the type-three q-binomial simplification stops

The obstruction to repeating the type-three algebra can be stated
without a parameter experiment. Expand the exact Newton polynomial
inside the physical cap. If \(M=N-1-i-l\), finite product
rearrangement gives
\[
\begin{split}
\mathcal U_{\epsilon,N}(w,r^i)
={}&\frac1{P_i}\sum_{l=0}^{N-1-i}
 q^{-l}r^{-l(l+1)/2}e_l(w)\,
 \frac{P_{i+l}}{P_l^{1+\epsilon}}\,S_{\epsilon}(i,l),\\
S_\epsilon(i,l)
={}&\sum_{h=0}^{M}
 \frac{(r^{-M};r)_h\,r^{-lh}}
      {P_h(r^{l+1};r)_h^\epsilon}.
\end{split}
\tag{12}
\]
To verify it, write the original private index as \(j=l+h\) and use
\[
(r^{-j};r)_l=(-1)^l r^{-jl+l(l-1)/2}
                  \frac{P_j}{P_{j-l}}.
\]
Every denominator in (12) has length below the physical zero.

For \(\epsilon=0\), the terminating q-binomial identity evaluates
\(S_0=(r^{-l-M};r)_M\), giving the proved physical \(U_0\)
reduction. For \(\epsilon=1\), the extra factor
\((r^{l+1};r)_h\) remains. It cannot be omitted: already
\(N=2,i=l=0\) gives \(S_0=2\) and \(S_1=3/2\).
This does not exclude another exact transformation, but it rules
out applying that unweighted binomial step to the type-four source.

The strongest currently proved cap packets are on correlated complex
endpoint images, rather than all the real physical outgoing indices
needed in (3). Moreover the
[reversed-cap theorem, Proposition 2](research_mixed_reversed_cap_assembly.md)
proves that the nested positive cap profile exceeds the calibrated
terminal type-four phase at every actual type-four reference.
Thus taking absolute values at both remaining levels does not finish
the desired comparison. A coherent estimate for the shifted and
unshifted transforms in (8), or a complete two-index deformation
retaining their boundary currents, remains necessary. The identities
above do not promote a local packet to that global estimate.

