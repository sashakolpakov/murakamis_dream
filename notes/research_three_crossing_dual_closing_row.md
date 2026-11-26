# The actual closing row and its backward transport

Research note, 3 November 2026.

The remaining observation of the next-crossing column has an exact
third-order backward recurrence with prescribed endpoint data. It
retains the free boundary and its first normal. Its frozen equation
also shows precisely where the existing single dominant-mode
argument cannot be applied unchanged: two dominant roots have
equal modulus halfway through the required real-index transport.
This is not an assertion that the observation vanishes.

## 1. The original row, including its boundary current

Use \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(\eta=(-1)^D\), and \(\kappa=e^{\pi iD^2/(2N)}\).
All matrices are the original Newton matrices. In particular
\[
 \begin{split}
 C_{jj}&=c_j=qQ^j+q^{-1}Q^{-j},&
 C_{j,j-1}&=-d_j,\qquad d_j=2-Q^j-Q^{-j},\\
 L&=JCJ=C^T,&
 P_N(w)&=2T_N(w/2)+2 .
 \end{split}                                                     \tag{1}
\]
Write \(\mathbf e(w)^T=(e_0(w),\ldots,e_D(w))\) for the whole
Newton evaluation row, and define the actual remaining row
\[
 \ell(w)=\mathbf e(w)^TJM^2,\qquad
 \gamma=MJM^3\mathbf e_0,\qquad
 F_N(w)=\ell(w)\gamma.                                           \tag{2}
\]
The row in (2), rather than an auxiliary Fourier character, is
the observation needed for the adjacent \(+3,+3\) pendant.

Let \(L_j=M^{-j}LM^j\). The original exact trace recursion gives
\[
 L_2=8qI-qCL_1-q^2L,\qquad
 (L_1)_{jj}=4qQ^j-q(1+Q)Q^{2j},\qquad
 (L_1)_{j,j+1}=(L_1)_{j+1,j}=-(1-Q^{j+1})^2.                    \tag{3}
\]
These are the same matrices and ordering as in
[the boundary-current theorem](research_three_crossing_boundary_current.md),
Section 3.

**Proposition 1.** At every level, as an ordinary polynomial
identity in the unreduced boundary variable,
\[
 \boxed{\qquad
 \ell(w)(L_2-wI)
       =-\frac{\eta\kappa^2}{N^2}P_N(w)\mathbf e_0^T,\qquad
 \ell_D(w)=\kappa^2 .
 \qquad}                                                       \tag{4}
\]
Here \(\mathbf e_0^T\) denotes the first coordinate row.
The matrix \(L_2\) has lower bandwidth two and upper bandwidth
one. Its upper diagonal is
\[
                 (L_2)_{j-1,j}=Q^j(1-Q^j)^2\ne0
                                      \quad(1\le j<N).           \tag{5}
\]
Consequently the columns \(D,D-1,\ldots,1\) of (4), together
with the displayed last component, determine the whole actual
row by backward recursion. No inverse of a dense matrix is
needed, and no growing solution is chosen independently of
the original endpoint.

**Proof.** The original Newton recurrence, including its last
degree, is
\[
 \mathbf e(w)^T(C-wI)
                     =-\eta P_N(w)\mathbf e_D^T/N^2.             \tag{6}
\]
Since \(JL=CJ\), multiplication by \(JM^2\) proves (4):
\[
 \ell(L_2-wI)=\mathbf e(w)^T(C-wI)JM^2.
 \]
The first row of \(M^2\) is \(\kappa^2\mathbf e_0^T\).
Its last column has only its last entry, equal to
\(\kappa^2\). This also proves \(\ell_D=\kappa^2\).

The bandwidth follows from (3). For its upper diagonal,
\[
 \begin{split}
 (L_2)_{j-1,j}
  &=q c_{j-1}(1-Q^j)^2+q^2d_j\\
  &=(1-Q^j)^2\{q^2Q^{j-1}+Q^{-j+1}-q^2Q^{-j}\}\\
  &=Q^j(1-Q^j)^2 ,
 \end{split}
 \]
using \(Q=q^2\) and \(d_j=-Q^{-j}(1-Q^j)^2\).
The factor never vanishes at the listed indices. In column
\(j\), the only not-yet-determined component is \(\ell_{j-1}\);
the other possible components are \(\ell_j,\ell_{j+1},\ell_{j+2}\).
This proves the recursive assertion. The remaining column
zero is the prescribed current in (4), not a new freely
chosen boundary condition. \(\square\)

The exact triangular formula for \(JM^2\) also gives
\(\deg_w\ell_j\le D-j\).
Thus differentiating (4) retains all ordinary boundary normals:
\[
 \ell^{(m)}(L_2-wI)
     =m\ell^{(m-1)}
       -\frac{\eta\kappa^2}{N^2}P_N^{(m)}(w)\mathbf e_0^T
                         \quad(m\ge1).                          \tag{7}
\]
In particular, at \(w=-2\),
\[
 \ell(-2)(L_2+2I)=
 \begin{cases}
  0,&N\ \text{odd},\\
  4\kappa^2\mathbf e_0^T/N^2,&N\ \text{even},
 \end{cases}
 \qquad
 \ell'(-2)(L_2+2I)=\ell(-2)-\kappa^2\mathbf e_0^T.                \tag{8}
\]
Indeed \(P_N(-2)=2(-1)^N+2\) and
\(P_N'(-2)=(-1)^{N-1}N^2\).
Even at odd levels the first-normal equation is therefore
inhomogeneous.

## 2. A specific obstruction to a uniform one-mode proof

For backward distance \(r=D-j\), normalize the row by
\[
                  u_r=\kappa^{-2}S_r^2\,\ell_{D-r}(-2).
                                                                    \tag{9}
\]
This removes the endpoint sine-factorial denominator; \(u_0=1\).
We now compute the frozen equation at \(r/N=1/2\). This is
an algebraic statement about (3)--(5), not an assumed
asymptotic of its solution.

In a frozen right-acting symbol let \(z=Q^j\) and let \(E\)
denote the backward shift. At \(q\to1\),
\[
 \begin{split}
 C&=z+z^{-1}-(2-z-z^{-1})E,\\
 L&=z+z^{-1}-(2-z-z^{-1})E^{-1},\\
 L_1&=4z-2z^2-(1-z)^2(E+E^{-1}),\qquad
 L_2=8-CL_1-L.
 \end{split}                                                     \tag{10}
\]
For a left row the same symbol uses
\(E=\ell_{j+1}/\ell_j\).
At \(z=-1\), put \(d=2-z-z^{-1}=4\).
If \(\Lambda\) is a backward ratio for the normalized variable
in (9), then \(E=d/\Lambda=4/\Lambda\). Substitution into
\(L_2+2=0\) gives
\[
 L_2+2=-16-32E-16E^2-4E^{-1},\qquad
 \boxed{\quad \Lambda^3+16\Lambda^2+128\Lambda+256=0.\quad}        \tag{11}
\]

**Proposition 2.** At the half-period in (11), exactly two
roots are dominant, and their moduli are equal.

**Proof.** The real cubic in (11) is strictly increasing on
the real axis, since its derivative
\(3\Lambda^2+32\Lambda+128\) has negative discriminant and
positive leading coefficient. Its real root \(a\) lies in
\((-3,-2)\), by evaluating the cubic at these two integers.
The other roots are a nonreal conjugate pair \(b,\overline b\).
Their product gives
\[
                       |b|^2=-256/a>256/3>9^2,
 \]
while \(|a|<3\). Thus they are the two dominant roots and
have exactly equal modulus. \(\square\)

The actual next-crossing Gaussian window is centered at
\(j/N=x_*\in(1/3,1/2)\), as proved in
[the next-crossing Fourier theorem](research_three_crossing_next_crossing_fourier.md).
Backward transport from the prescribed endpoint \(j=D\)
to that window therefore passes through \(r/N=1/2\).
There cannot be a uniform strict gap between a single largest
root and all others on that entire real transport interval.
The equality persists under a common scalar phase correction
or a scalar normalization of the recurrence.

This is a limitation of that particular proof method. It does
not establish cancellation, failure of an observable overlap,
or any loss relative to the geometric exponential rate.
Raw row and vector norms need not have that geometric rate
in the first place. A two-mode connection calculation, or
transport along a justified complex contour, could still
control the actual row.

Equations (4)--(8) provide the exact dual problem for such a
calculation. The already proved Gaussian Fourier window
does not by itself select its connection coefficient.

## 3. Finite verification

The focused
[checker](../experiments/check_three_crossing_dual_closing_row.py)
constructs the original crossing matrix independently of (3),
then checks its conjugated matrix, upper diagonal, full boundary
row and first normal at \(w=-2\) and at a nonreal boundary.
The [saved 100-digit result](../repro/results/research-three-crossing-dual-closing-row.json)
contains 1,362 finite comparisons at levels \(2,\ldots,10\)
and both crossing signs. These are convention checks;
Propositions 1--2 are the proofs, and no asymptotic rate or
connection coefficient is inferred from the finite residuals.
