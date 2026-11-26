# An exact odd-level support identity for the marked bipyramid

This is a finite polynomial identity for the original opposite-offset
bipyramid source. It is independent of any limiting spectral estimate.
It concerns Newton path indices, not a change of auxiliary colors or
the replacement of a source factor by a covariant coupon.

Let the equator have even size \(m\ge6\). Write its faces as
\(z_0,\ldots,z_{m-1}\), protect the north face and \(z_0\), and retain
one south variable \(S\). Thus the original ordered factors are
\[
 F_j=
 \begin{cases}
 H_{V_N(\sigma_j),N}(0,z_{j-1},z_{j+1},z_j),&j\text{ odd},\\
 H_{V_N(\sigma_j),N}(S,z_{j+1},z_{j-1},z_j),&j\text{ even}.
 \end{cases}
 \tag{1}
\]
Indices are cyclic, and the source extracts
\([
 S^d z_1^d\cdots z_{m-1}^d
]\prod_jF_j\) after \(z_0=0\), where \(d=N-1\).
Here
\[
 \chi_N(\sigma)=2T_N(\sigma/2)+2,\qquad
 V_N(\sigma;C)=
 \frac{\chi_N(\sigma)-\chi_N(C)}{\sigma-C}
 \tag{2}
\]
is polynomial functional calculus before root specialization. The raw
upper-triangular Casimir has diagonal
\(c_r=2\cos((2r+1)\pi/N)\), first upper diagonal
\(-s_r^2(x+y)\), and second upper diagonal
\(-s_rs_{r-1}xy\), with \(s_r=2\sin(r\pi/N)\).

Let \(S_N^{\mathrm{full}}\) denote this shared coefficient and
\(S_N^{\mathrm C}\) the same coefficient after restricting every
original resolvent path to CROSS. These restrictions are performed
before multiplying the original face polynomials.

**Finite support identity.** If \(N=2h+1\) is odd and
\(\sigma_j=-2\) for every \(j\ne0\), then
\[
 S_N^{\mathrm{full}}(\sigma_0,-2,\ldots,-2)
 =S_N^{\mathrm C}(\sigma_0,-2,\ldots,-2)
 \quad\text{for every }\sigma_0\in\mathbb C.
 \tag{3}
\]
In particular the unsplit remainder vanishes identically on this line
of the spectral parameter space. There is no assertion here about its
size off that line.

To prove this, first retain the complete path expression for the
\((i,j)\)-entry of \(V_N\), including all unused diagonal factors.
At odd level the central node is \(c_h=-2\). If \(j<h\) or
\(i>h\), that central node is unused by every path and contributes
the factor \(\sigma-c_h\). Consequently at \(\sigma=-2\) those
two one-sided blocks vanish identically in the face variables. Only
\[
 i\le h\le j.
 \tag{4}
\]
can remain. This is exactly the odd-level CROSS support, with the
central row retained. Some paths that jump over the central row can
also vanish, which only reduces the support; no such path is restored.

Every factor other than \(F_0\) therefore already equals its CROSS
restriction. The protected input face of \(F_1\) forces its row to
be zero. Its column \(j_1\) satisfies \(j_1\ge h\) by (4).
Since its north outer variable is zero, this factor has
\(z_1\)-degree exactly \(j_1\), hence at least \(h\).
Similarly the protected output of \(F_{m-1}\) forces its column to
be \(d\); its row \(i_{m-1}\le h\). Thus it has
\(z_{m-1}\)-degree \(d-i_{m-1}\ge h\).

Consider now a monomial of the exceptional factor \(F_0\), whose
original row and column are \(i_0,j_0\). Its middle face degrees are
\(i_0\) on \(z_1\) and \(d-j_0\) on \(z_{m-1}\).
All contributions from every other factor are nonnegative degrees.
The unchanged target \(d=2h\) on these two shared faces therefore
implies
\[
 i_0+h\le2h,\qquad d-j_0+h\le2h.
 \tag{5}
\]
Hence \(i_0\le h\le j_0\). The exceptional factor is forced to
be CROSS as well. This is a termwise statement about the original
coefficient support, so it proves (3) with all signs, the shared south
demand, and all root-normal data intact.

This proof uses bare \(V_N(-2)\), not the regularized positive
full-reference numerator used in odd-level energy comparisons. The
latter includes a derivative and need not have the same support.
No filling functional has been applied to (3), so no normal or
endpoint current has been discarded.
