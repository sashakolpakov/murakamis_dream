# The actual pointed main-color adjoint and its cut flux

Research note, 17 November 2026. The bounded-jet main-color system
has an inhomogeneous terminal adjoint without an invertibility or
special-fiber rank assumption. Its pairing with the original initial
source, and its flux across every intervening cut, are exactly the
original complete quantum period. Every retained normal component is
part of this identity. Positive energy and the terminal adjoint are
different constructions.

This is an exact source identity. It does not estimate the terminal
pairing, identify a geometric solution line, or prove its nonvanishing.

## 1. The actual finite system and its terminal row

Use the actual operator, fixed pointing and uniform jet budget of
[G, Sections 1--2 and 5](pointed_a_gram_period.md). Write
\[
 \mathcal A=\sum_{i=0}^{d}a_i(q,M)T^i,
 \qquad TM=qMT,
 \qquad
 \sum_i a_i(q,-q^j)C_{j+i}(q)=0.
 \tag{1}
\]
Here the reduced actual colors have the original normalization,
\(q_N=e^{\pi i/N}\), and \(C_N(q_N)=\langle K\rangle_N\).
Fix the starting color \(j_0\) and jet budget \(B\) prescribed in G.
Take \(N\ge j_0+d\) sufficiently large for its uniform pole budget.
Set \(b=B+1\), let \(e_0\in\mathbb C^b\) select the constant jet,
and use the scaled jet coordinates
\[
 y_j=(C_j(q_N),N^{-1}y^{\rm raw}_{j,1},\ldots,
                      N^{-B}y^{\rm raw}_{j,B})^{\mathsf t},
 \quad j_0\le j\le N,
\]
where the raw coordinates are coefficients in
\(t=q/q_N-1\). These symbols also denote arbitrary solutions of
the resulting truncated system, not only the actual full-jet lift.

Keep initial and recurrence rows as separate labelled sets. Let
\(I_0y=(y_{j_0},\ldots,y_{j_0+d-1})\), and put
\[
 (Hy)_j=\sum_{i=0}^d A_i(j)y_{j+i},
       \qquad j_0\le j\le N-d,
 \qquad
 M_N=\begin{pmatrix}I_0\\H\end{pmatrix},
 \qquad
 b_N=\begin{pmatrix}b^{\rm in}\\0\end{pmatrix}.
 \tag{2}
\]
The matrices \(A_i(j)\) are the actual truncated multiplication
blocks, conjugated by \(\operatorname{diag}(1,N^{-1},\ldots,N^{-B})\).
For example a monomial \(q^aM^c\) contributes
\((-1)^cq_N^{a+cj}N^{-r}\binom{a+cj}{r}\) on its \(r\)-th
subdiagonal. Thus (2) has the original full jet content and fixed
block bandwidth. Its blocks are uniformly bounded; no leading
coefficient is divided out at \(q_N\).

The source \(b^{\rm in}\) consists of the fixed small-color jets.
The conclusions of G that will be used are exactly
\[
 M_Ny=b_N\text{ is solvable},\qquad
 \ker M_N\subset\ker R_N,
 \qquad R_Ny=(e_0^*y_j)_{j=j_0}^N.
 \tag{3}
\]
They include singular recurrence steps and possibly nonunique
higher jets. Define the terminal row and its actual value by
\[
 \ell_Ny=e_0^*y_N,
 \qquad Z_N=\langle K\rangle_N=\ell_Ny.
 \tag{4}
\]
An asterisk is the ordinary conjugate transpose at the fixed complex
embedding. All scalar pairings below are complex pairings; no real
or positive value is asserted.

## 2. The terminal adjoint affine space

**Theorem 1.** The affine space
\[
 \mathcal P_N=\{p:M_N^*p=\ell_N^*\}
 \tag{5}
\]
is nonempty. It is a translate of \(\ker M_N^*\). For every
\(p\in\mathcal P_N\) and every solution of (2),
\[
                         Z_N=p^*b_N.
 \tag{6}
\]
This value is independent of both choices. In particular (5) uses
only the known pointed matrix and the prescribed terminal row; its
definition does not insert the unknown value \(Z_N\).

**Proof.** Equation (3) implies \(\ell_N\ker M_N=0\).
Finite-dimensional orthogonal complements give
\(\operatorname{im}M_N^*=(\ker M_N)^\perp\), so (5) is solvable.
Subtracting two solutions proves its asserted translation space.
Now
\(p^*b_N=p^*M_Ny=\ell_Ny=Z_N\).
If \(p\) changes by \(h\in\ker M_N^*\), then
\(h^*b_N=h^*M_Ny=0\). Changes of \(y\) lie in
\(\ker M_N\) and are annihilated by \(\ell_N\). This proves
all assertions. \(\square\)

Equivalently the linear functional on \(\operatorname{im}M_N\)
given by \(M_Nx\mapsto\ell_Nx\) is well defined, and (5)
is its set of vector representatives. It has a unique representative
orthogonal to \(\ker M_N^*\). Existence of this representative
places no upper bound on its norm.

## 3. Exact flux, including the initial and terminal jumps

Write \(p=(\alpha,v)\) according to (2), with
\(\alpha=(\alpha_j)_{j_0\le j<j_0+d}\) and
\(v=(v_j)_{j_0\le j\le N-d}\). The adjoint equation is
\[
 H^*v=\ell_N^*-I_0^*\alpha.
 \tag{7}
\]
Extend \(v_j\) by zero outside its recurrence index set. Also
extend \(y_j\) by zero outside the color interval. For an integer
cut \(c\), define the finite forward flux
\[
 \mathcal W_c(v,y)=
 \sum_{\substack{j_0\le j\le N-d,\ 0\le i\le d\\
                         j\le c<j+i}}
                  v_j^*A_i(j)y_{j+i}.
 \tag{8}
\]
It uses only the recurrence dual blocks with
\(c-d+1\le j\le c\) and the color blocks
\(c+1\le j+i\le c+d\), intersected with their actual ranges.
There is no deleted normal, periodic identification, or implicit
extension of the recurrence past its last row.

**Theorem 2.** For every original solution and every adjoint (5),
\[
 \mathcal W_c-\mathcal W_{c-1}
   =\mathbf 1_{j_0\le c<j_0+d}\alpha_c^*b_c^{\rm in}
                         -\mathbf 1_{c=N}Z_N.
 \tag{9}
\]
In particular
\[
 \mathcal W_{j_0-1}=0,\qquad
 \mathcal W_c=Z_N\quad(j_0+d-1\le c\le N-1),
 \qquad \mathcal W_N=0.
 \tag{10}
\]
Each intervening cut therefore gives the same original scalar,
independently of the chosen representatives in both affine spaces.

**Proof.** For arbitrary \(y,v\), adding the terms whose row first
appears at \(c\) and removing the terms whose column is \(c\) gives
\[
 \mathcal W_c-\mathcal W_{c-1}
       =v_c^*(Hy)_c-((H^*v)_c)^*y_c.
 \tag{11}
\]
The first term is understood to be zero outside the recurrence
index set. Indeed its \(i=0\) term cancels the \(j=c\) term of
the second expression; all other terms are exactly the two changes
in (8). In the actual system \(Hy=0\). Substitution of (7),
the prescribed initial values and (4) proves (9).
The sum (8) is empty before \(j_0\) and at or beyond \(N\).
Summing (9) therefore gives (6) and then (10). \(\square\)

Formula (8) is a fixed-size block pairing
\(v_{\rm left}^*G_cy_{\rm right}\), where the block in row \(j\)
and column \(k\) is \(A_{k-j}(j)\) if \(0\le k-j\le d\), and
zero otherwise. Uniform boundedness in (2) gives
\[
 |Z_N|\le C\|v_{\rm left}\|\,\|y_{\rm right}\|
                     \quad(j_0+d-1\le c<N).
 \tag{12}
\]
The constant depends on the fixed operator and jet budget, not the
cut or level. Both packets in (12) contain all \(B+1\) jet
components. An estimate for ordinary constant colors alone cannot
be substituted for the full packets. Conversely (12) is an upper
bound on the complex pairing, not a lower bound from either norm.

## 4. Exact covariance under the geometric weights

Give each color block an arbitrary positive weight \(w_j\).
Let \(W_c\) act on columns by these weights, and let \(W_r\)
act on an initial row by its prescribed color weight and on a
recurrence row by its label \(j\). This is the row convention of
[A, Section 1](actual_pointed_a_bulk_agmon_energy.md). Define
\[
 u=W_cy,\quad L=W_rM_NW_c^{-1},\quad b^w=W_rb_N,
 \quad p^w=W_r^{-1}p,\quad \ell^w=\ell_NW_c^{-1}.
 \tag{13}
\]
Then, exactly,
\[
 Lu=b^w,\qquad L^*p^w=(\ell^w)^*,\qquad
                   (p^w)^*b^w=\ell^wu=Z_N.
 \tag{14}
\]
These changes give a bijection of the two adjoint affine spaces,
including their homogeneous translation spaces.

The weighted recurrence block is
\(A_i^w(j)=w_jA_i(j)w_{j+i}^{-1}\), and its dual block is
\(v_j^w=w_j^{-1}v_j\). Every individual summand satisfies
\[
                  (v_j^w)^*A_i^w(j)u_{j+i}
                         =v_j^*A_i(j)y_{j+i}.
 \tag{15}
\]
Thus the weighted cut flux, all initial jumps and the terminal jump
are unchanged. This includes \(w_j=\exp(N\varphi(j/N))\) for
any of the real source-anchored or tilted geometric weights in A.
No eikonal or spectral-gap assumption is needed for (13)--(15).

If instead the weighted adjoint is normalized to have the unscaled
unit terminal row \(\ell_N\), its representative is
\(\widehat p^w=w_Np^w\). Its flux and source pairing equal
\(w_NZ_N\), and recovery of the original scalar requires
the factor \(w_N^{-1}\). This normalization factor cannot be
discarded when estimating a geometric exponential rate.

## 5. The positive energy has a different dual source

For the same actual \(u\), the exact Agmon energy is
\[
                  u^*L^*Lu=\|b^w\|^2.
 \tag{16}
\]
Its row vector \(p^{\rm en}=Lu=b^w\) has recurrence component
zero. Consequently its cut flux (8), with the weighted blocks,
is identically zero. Moreover
\(L^*p^{\rm en}=L^*b^w\) is supported only in the initial
color blocks: the initial equations in \(L\) remain identity
equations. Since \(N\ge j_0+d\), it cannot equal the nonzero
terminal point source \((\ell^w)^*\).

The distinction is therefore exact in the original pointed system.
The positive value in (16) does not establish a sign or nonzero
value of (10). A useful weighted Green estimate for the complete
period must retain the actual terminal affine space (5), or its
weighted version (14), together with the original initial source.
The full cut formula makes those two boundary data explicit; it
does not bound their connection through turning or singular steps.

## 6. Coverage and complete proof sources

The cyclic transpose identity and the inhomogeneous Weyl-sector
Green column are already in
[W, Section 2](research_actual_weyl_green_obstruction.md).
The identity here concerns the noncyclic, pointed main-color
matrix with its complete bounded-jet repair. Its adjoint exists
unconditionally by G's kernel-annihilation theorem, and (9)
retains the literal initial and terminal cut jumps. No special-fiber
injectivity or Weyl identification is imported from W.

The complete proof sources, read in full, are:

- G: `pointed_a_gram_period.md`, SHA256
  `8de50a01f06b406e76325d09ea7d6c415afe6a4629c8d2380a809d447c64583c`.
  Its actual system, kernel-annihilation statement and scaled blocks
  are the inputs to Sections 1--3.
- A: `actual_pointed_a_bulk_agmon_energy.md`, SHA256
  `df1bccf577f5732dd7697bf2ae03901077d63b48f85820544dba10395391effd`.
  Its literal row weights and sourced energy are used in Sections 4--5.

The complete coverage comparison W was also read in full:
`research_actual_weyl_green_obstruction.md`, SHA256
`e934449b725e028822502185f2666c2e2203ce3816cf2dd774d94dac6791a3dd`.
All finite-dimensional adjoint and cut identities used above are
proved here. No numerical calculation or added scalar positivity
assumption enters the argument.
