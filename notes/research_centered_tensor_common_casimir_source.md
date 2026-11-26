# A shared affine Casimir equation for the original tensor

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

The three forced Rogers equations can be written with one symmetric
quantum trace potential and one common affine source. Their difference
recovers the exact common-Casimir relation without projecting or deleting
the forcing. On the complete finite generating grid the source vanishes
and gives homogeneous nearest-neighbor equations. This grid is an
invertible Fourier coordinate system on the whole tensor, including
the physical Casimir normals.

Common-Casimir balance was already proved in the centered compiler.
The result here is its explicit shared trace potential with the
initialized source retained. It is an algebraic consequence of the
forced Rogers theorem, not an independent source estimate or a global
geometric gap.

## 1. The tensor and its actual Casimir operator

Fix \(N\ge2\), and write
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 a=q^{-1},\quad \eta=(-1)^d,\quad
 \kappa=q^{d^2/2},\qquad D_N(t)=1-\eta t^N .
 \tag{1}
\]
Use the full original algebra
\(\mathcal H_N=\mathbb C[z]/(2T_N(z/2)+2)\), its original
Frobenius functional \(\phi\), and its centered basis \(f_j\).
Here \(T_N(\cos\theta)=\cos N\theta\). In particular
\[
 \phi(f_jf_k)=\delta_{jk},\qquad
 R^+=\sqrt N f_0,\quad R^-=\sqrt N f_d,\qquad
 C_{ijk}=\phi(f_if_jf_k).
 \tag{2}
\]
The unit, genuine turn and both original closing rows are those of
the centered compiler. No closing row is changed below.
Put
\[
 \mathcal F_N(t)=\sum_{j=0}^d f_jt^j,\qquad
 \mathcal C_N(x,y,z)
    =\phi(\mathcal F_N(x)\mathcal F_N(y)\mathcal F_N(z)),
 \qquad \mathcal D=D_N(x)D_N(y)D_N(z).
 \tag{3}
\]
The letter \(z\) is a generating argument in (3); the algebra
coordinate in the preceding quotient occurs only inside its factors.
For a polynomial \(F\) of degree below \(N\) in \(x\), define
\[
 \mathscr Z_xF
   =\frac{(1+ax)^2F(x/Q,y,z)-(1+x^2)F(x,y,z)}{x}.
 \tag{4}
\]
The numerator vanishes at \(x=0\), so this is a polynomial.
Indeed
\[
 \mathscr Z_x x^j
   =(Q^{-j}-1)x^{j-1}
      +2aQ^{-j}x^j+(a^2Q^{-j}-1)x^{j+1}.
 \tag{5}
\]
The first coefficient is zero at \(j=0\), and the last is zero at
\(j=d\), since \(a^2Q^{-d}=Q^{-N}=1\). Thus (4) preserves the
entire \(N\)-dimensional coefficient space and has no missing wrap
silently replaced by a cyclic arrow.

The centered Casimir recurrence is
\[
 zf_j=(Q^{-j-1}-1)f_{j+1}
           +2aQ^{-j}f_j+(Q^{-j}-1)f_{j-1}.
 \tag{6}
\]
Summing (6) against \(t^j\) proves that multiplication by the
actual Casimir on \(\mathcal F_N(t)\) is exactly (4).
Consequently the known common-Casimir identities are
\[
             \mathscr Z_x\mathcal C_N
       =\mathscr Z_y\mathcal C_N
       =\mathscr Z_z\mathcal C_N .
 \tag{7}
\]
This argument uses the full quotient, rather than its distinct-root
values.

## 2. One common affine equation

Let
\[
 s_1=x+y+z,\qquad s_2=xy+xz+yz,\qquad s_3=xyz,
 \qquad h=1+as_3,\qquad
 L=a-s_1-as_2+s_3,
 \tag{8}
\]
and retain the known nonzero source scalar
\[
                  \beta_N=\frac{(-1)^{N+1}\kappa^3}{N^{3/2}}.
 \tag{9}
\]

**Theorem 1.** The original polynomial tensor satisfies
\[
 \boxed{\qquad
      h\,\mathscr Z_i\mathcal C_N-L\mathcal C_N
                    =-\frac{\beta_N}{Q}\mathcal D,
                  \qquad i=x,y,z .
       \qquad}
 \tag{10}
\]
These are polynomial identities, including at \(h=0\).
Where \(h\ne0\), their shared quantum trace potential is
\[
            \Lambda_q=\frac{a-s_1-as_2+s_3}{1+as_3}.
 \tag{11}
\]
Thus all three affine equations have the same right side
\(-\beta_N\mathcal D/(Qh)\) after division by \(h\).

**Proof.** The exact forced Rogers equation, with its full initialized
normal and every norm factor, is
\[
 (1-Qxy)(1-Qxz)\mathcal C_N(Qx,y,z)
 -(1+qx)(1+qxyz)\mathcal C_N(x,y,z)
          =\beta_N\mathcal D\,\frac{x}{1+qx}.
 \tag{12}
\]
Its apparent pole is removable because \(1+qx\) divides \(D_N(x)\).
Replace \(x\) by \(x/Q\), using \(D_N(x/Q)=D_N(x)\):
\[
 (1-xy)(1-xz)\mathcal C_N
 -(1+ax)h\mathcal C_N(x/Q,y,z)
        =\frac{\beta_Nx\mathcal D}{Q(1+ax)}.
 \tag{13}
\]
Multiply by \(-(1+ax)\). The elementary symmetric expansion
\[
       h(1+x^2)+xL=(1+ax)(1-xy)(1-xz)
 \tag{14}
\]
then gives \(x\) times (10). The removable value at \(x=0\)
proves that equation everywhere. Permutation proves the other two.
No division by \(h\), no boundary-source deletion and no choice of
a homogeneous solution occurred. \(\square\)

Conversely, (10) multiplied by \(x\), together with (14), gives
(13) on \(1+ax\ne0\); the original removable identity extends it.
Thus (10) repackages the initialized first-order connection.
Its content is the explicit common potential and source, rather
than a new independent constraint on \(\mathcal C_N\).
Subtracting two equations gives
\(h(\mathscr Z_x-\mathscr Z_y)\mathcal C_N=0\), and hence (7),
since \(h\) is a nonzero polynomial.

As a normalization check, the constant coefficient of (10) is
\[
        (Q^{-1}-1)C_{100}+aC_{000}=-\beta_N/Q.
 \tag{15}
\]
Equivalently
\[
                    (Q-1)C_{100}-qC_{000}=\beta_N .
 \tag{16}
\]
This is the original nonzero first-coefficient source identity.
Replacing the affine equation by its homogeneous part would violate it.

## 3. The finite generating grid and its endpoint

For \(0\le j<N\), put
\[
 \xi_j=(j+\tfrac12)/N,\qquad
 t_j=-e^{-2\pi i\xi_j}=-q^{-1}Q^{-j},\qquad
 \gamma_j=\exp\!\left[-\frac{\pi i d}{N}(j-d/2)\right].
 \tag{17}
\]
Then \(D_N(t_j)=0\), and \(t_j/Q=t_{j+1}\), with the index read
modulo \(N\). Direct finite Fourier summation in the centered basis
gives
\[
 \mathcal F_N(t_j)=\sqrt N\,\gamma_je_j,\qquad
 \mathcal C_N(t_i,t_j,t_k)
           =N^{3/2}\gamma_i\gamma_j\gamma_k\,\tau_{ijk},
 \quad \tau_{ijk}=\phi(e_ie_je_k).
 \tag{18}
\]
For example, the coefficient of \(e_r\) in the first identity is
\[
 \frac{e^{-\pi i d(r-d/2)/N}}{\sqrt N}
       \sum_{b=0}^{N-1}e^{2\pi ib(r-j)/N}.
 \tag{19}
\]
This proves (18), including both parities.

**Corollary 2.** Restricting (10) to this grid gives the exact
homogeneous nearest-neighbor equations
\[
 \begin{split}
 &h(t_i,t_j,t_k)\!
 \left[
   \frac{(1+at_i)^2}{t_i}
             \mathcal C_N(t_{i+1},t_j,t_k)
       -(t_i+t_i^{-1})\mathcal C_N(t_i,t_j,t_k)
 \right]\\
 &\hspace{35mm}
       -L(t_i,t_j,t_k)\mathcal C_N(t_i,t_j,t_k)=0 ,
 \end{split}
 \tag{20}
\]
and their permutations. At \(i=d\), \(t_d=-q\) and
\(1+at_d=0\). Thus the coefficient of the apparent cyclic neighbor
is exactly zero, and the bracket is
\((q+q^{-1})\mathcal C_N(t_d,t_j,t_k)\).
The original absent endpoint arrow is retained.

The grid evaluation map on polynomials of separate degree below \(N\)
is an invertible tensor product of discrete Fourier transforms.
Accordingly the *full grid values* in (18) retain all \(N^3\)
original tensor coordinates and their physical Casimir Hermite data.
This is not evaluation at only the distinct physical Casimir roots.
The homogeneous constraints alone are weaker data: for example the
zero tensor satisfies them, and (16) is still needed to retain the
specified source.

On an active grid entry the denominator in (11) is controlled.
The original positive Newton support is
\[
 i+j,\ i+k,\ j+k\le d,\qquad S=i+j+k\ge d .
 \tag{21}
\]
It gives \(d\le S\le3d/2\). At the corresponding grid point
\[
                  h=1-Q^{-S-2}.
 \tag{22}
\]
The interval \(N+1\le S+2\le3(N-1)/2+2<2N\)
contains no multiple of \(N\). Therefore
\[
        |h|\ge2\sin(\pi/N)\ge4/N
          \quad\hbox{on every nonzero entry in (18)}.
 \tag{23}
\]
No division by \(h\) is asserted on inactive entries where it vanishes.
The lower bound is polynomial in the level, not an estimate of
the global closing period.

There is an actual boundary contact on that excluded divisor.
For every \(N\ge2\), choose any nonnegative \(i,j,k\) with
\(i+j+k=d-1\). The tensor entry is zero by (21), and (22)
gives \(h=0\). But \(i<d\), and the shifted entry
\((i+1,j,k)\) has total \(d\) and all pairwise sums at most \(d\);
its Newton coefficient in (18) is strictly positive. Its arrow
coefficient \((1+at_i)^2/t_i\) is nonzero. Consequently
\[
 \mathcal C_N(t_i,t_j,t_k)=0,\qquad h(t_i,t_j,t_k)=0,
 \qquad(\mathscr Z_x\mathcal C_N)(t_i,t_j,t_k)\ne0 .
 \tag{23a}
\]
The same argument applies to the other two coordinates.
Equation (20) becomes \(0=0\) on this layer, rather than excluding
its nonzero Casimir current. This is a general finite boundary
phenomenon, with no selected knot or filling example.

## 4. What the equation preserves, and what it does not prove

There are two different exact operations. On the finite generating
grid, \(D_N(t_j)=0\) and (20) follows. In the nonnegative Taylor
coefficient assembly, the relevant auxiliary quotient is
\(\mathbb C[x,y,z]/(x^N,y^N,z^N)\), where each \(D_N=1\).
There the right side of (10) is \(-\beta_N/Q\), and, after
division by the unit \(h\), is
\[
        -\frac{\beta_N}{Q}
                     \sum_{r=0}^{N-1}(-a)^r x^ry^rz^r.
 \tag{24}
\]
It is nonzero. One cannot delete this term in the original coefficient
period by using its vanishing under a different finite-grid operation.
All original leaves, turns and closure rows must accompany either
exact coordinate representation.

For fixed \(|x|,|y|,|z|\le1\), (10) also gives the elementary absolute
bound
\[
       |h\,\mathscr Z_i\mathcal C_N-L\mathcal C_N|
                                  \le8N^{-3/2}.
 \tag{25}
\]
This is a pointwise generating-function residual, not a full boundary
packet norm bound. Where \(\mathcal C_N\) is already known to have
positive exponential height, it is a relatively small source current.
It does not prove such height or a nonzero closing coefficient.

Finally, where \(1+s_3\ne0\),
\[
          \Lambda_q\longrightarrow
                 1-\frac{s_1+s_2}{1+s_3}.
 \tag{26}
\]
This is the previously identified bulk critical trace.
Equation (10) retains its exact quantum correction and source.
It does not show that every boundary or escaping critical stratum
of an assembled short-filled period satisfies the full knot-group
relations. In particular it gives no representation-volume bound
for a raw Ward return considered in isolation, no source-preserving
deletion of that return, and no new global spectral gap.

## Complete proof sources and coverage

Both complete proof sources were read at the matching pins:

| Source | SHA-256 |
|---|---|
| [Original centered compiler](research_centered_fourier_conway_compiler.md) | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |
| [Initialized forced Rogers connection](research_centered_tensor_forced_rogers_connection.md) | 0d2ed84d814c892754f87dcda16d50167dc50acb845538720aa9e6abb9e3d8d7 |

The first already supplies the common-Casimir recurrence, full
positive Newton support, invertible Fourier coordinates and original
source closures. The second supplies the exact affine equation
with its initialized normal, as well as the full coefficient-period
rule. The shared potential, cancellation (14), grid specialization
and active-denominator bound are derived above.
The complete generating-section theorem already supplies a forced
Casimir equation for one generating leg; no novelty is claimed for
that operator, common-Casimir balance, or finite Fourier inversion.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
