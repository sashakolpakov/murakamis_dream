# A canonical finite splitting of the full Hermite filling kernel

Private written proof, 18 November 2026.

The physical circle basis gives an explicit endomorphism whose image
is exactly the kernel of the original filling functional. Its
one-dimensional complement has a specified period normalizer.
The endomorphism and its inverse on that kernel have polynomial
norm bounds, for every fixed signed crossing power.

This is finite algebra on the original full Hermite space. It neither
replaces the closing functional nor supplies a lower bound for its
value on an exterior source. In particular the conjugated
endomorphism below is not identified with off-grid Gaussian averaging.

The sole complete proof directs are **N**, the physical finite Newton
calculus, and **F**, the actual Fourier--Hermite crossing-circle
kernel. Their exact paths and pins are recorded at the end.

## 1. The physical space, row and circle basis

Fix \(N\ge2\), \(d=N-1\), and the original lifts
\[
 q=e^{\pi i/N},\qquad \kappa=q^{d^2/2},\qquad
 \mathcal H_N=\mathbb C[z]/(\chi_N),\qquad
 \chi_N(z)=2T_N(z/2)+2.
 \tag{1}
\]
The quotient includes all first normals at double roots and the
single value at the odd-level simple root. Let \(R\) be the actual
physical crossing of N, with its Cartan phase. Its values at every
root are nonzero, so it is a unit of the full quotient. Negative
powers below mean its actual inverse.

The original pivotal circle operators are the basis
\[
 L_j=(-1)^{j-1}U_{j-1}(z/2),\qquad 1\le j\le N.
 \tag{2}
\]
They are a basis because their degrees are \(j-1\), with nonzero
leading coefficients. Use their coefficient norm
\[
 \left\|\sum_{j=1}^N c_jL_j\right\|_\circ=\sum_{j=1}^N|c_j|.
 \tag{3}
\]
This is a specified finite norm, not an energy defined using an
unknown knot value.

Write \(\phi\) for the actual cylindrical closing functional of N.
Its normalization and that of an integral filling are
\[
 \phi(f)=(-1)^dN^2[z^d](f\bmod\chi_N),\qquad
 \phi_n(f)=\phi(R^nf),\qquad n\in\mathbb Z.
 \tag{4}
\]
Thus
\[
 \phi(L_j)=0\quad(j<N),\qquad \phi(L_N)=N^2.
 \tag{5}
\]
All peripheral or framing factors already outside this physical
pair row remain outside it. Nothing is divided by a quantum
dimension or by the possibly nilpotent operator \(L_N\).

## 2. The zero-twist average and its exact inverse off one line

On \(z=-2\cos t\), the actual circle basis has the identity
\[
                         L_j(-2\cos t)=\frac{\sin(jt)}{\sin t}.
 \tag{6}
\]
For the unique polynomial representative of degree \(<N\), average
its sine-weighted value over one grid cell:
\[
 \frac1{\sin t}\int_{-1/2}^{1/2}
   \sin(t+2\pi\rho/N)\,
   f(-2\cos(t+2\pi\rho/N))\,d\rho .
 \tag{7}
\]
Equation (6) shows directly that (7) is again a polynomial of
degree \(<N\), and its action on the basis is
\[
 K_0L_j=\lambda_jL_j,\qquad
 \lambda_j=\frac{\sin(j\pi/N)}{j\pi/N}.
 \tag{8}
\]
At sine zeros (7) is interpreted by this polynomial identity.
Equivalently (8) defines \(K_0\) intrinsically in the specified
physical basis; it does not require choosing another representative.

For \(1\le j<N\), \(\lambda_j>0\), whereas \(\lambda_N=0\).
Consequently
\[
 \ker K_0=\mathbb C L_N,\qquad
 \operatorname{im}K_0=\ker\phi.
 \tag{9}
\]
Define
\[
 G_0L_j=
 \begin{cases}\lambda_j^{-1}L_j,&j<N,\\0,&j=N,\end{cases}
 \qquad
 P_0f=\frac{\phi(f)}{N^2}L_N .
 \tag{10}
\]
Then the complete exact identities are
\[
 K_0G_0=G_0K_0=I-P_0,\qquad
 G_0P_0=P_0G_0=K_0P_0=P_0K_0=0.
 \tag{11}
\]
The function \(\sin x/x\) decreases on \(0<x<\pi\):
the numerator of its derivative is \(x\cos x-\sin x\), whose
derivative is \(-x\sin x<0\) and whose value at zero is zero.
Since \(\sin(\pi/N)\ge2/N\), this proves
\[
 \|K_0\|_\circ\le1,\qquad \|P_0\|_\circ=1,\qquad
                 \|G_0\|_\circ\le\frac{\pi N}{2}.
 \tag{12}
\]
These are induced operator norms. The estimate includes \(N=2\).

## 3. Conjugation by the actual signed crossing

Let \(M_f\) denote multiplication by \(f\) in the full quotient.
For every signed integer \(n\), set
\[
 \widetilde K_n=M_{R^{-n}}K_0M_{R^n},\qquad
 G_n=M_{R^{-n}}G_0M_{R^n},\qquad
 u_n=\frac{R^{-n}L_N}{N^2},\qquad
 P_nf=u_n\phi_n(f).
 \tag{13}
\]
All operations in (13) are on quotient classes, with every
Hermite normal retained. Equations (5), (9)--(11) give
\[
 \phi_n(u_n)=1,\qquad
 \ker\widetilde K_n=\mathbb C u_n,\qquad
 \operatorname{im}\widetilde K_n=\ker\phi_n,
 \tag{14}
\]
\[
 \widetilde K_nG_n=G_n\widetilde K_n=I-P_n,\qquad
 G_nP_n=P_nG_n=\widetilde K_nP_n=P_n\widetilde K_n=0.
 \tag{15}
\]
In particular \(\widetilde K_n\) has rank \(N-1\), and \(G_n\)
is its genuine two-sided inverse on \(\ker\phi_n\). Every original
boundary class has the exact decomposition
\[
                 f=\widetilde K_nG_nf+u_n\phi_n(f).
 \tag{16}
\]
Thus the sequence
\[
 0\longrightarrow\mathbb C
 \mathop{\longrightarrow}^{c\mapsto cu_n}\mathcal H_N
 \mathop{\longrightarrow}^{\widetilde K_n}\mathcal H_N
 \mathop{\longrightarrow}^{\phi_n}\mathbb C
 \longrightarrow0
 \tag{17}
\]
is exact, with the displayed splitting. The last coordinate is
the original period itself, not a substitute for it.
This is a sequence of complex vector spaces: \(\ker\phi_n\)
is not asserted to be an ideal, and (17) is not a quotient-algebra
or \(\mathcal H_N\)-module construction.

## 4. Polynomial conditioning with no deleted normal directions

Here is an elementary multiplication estimate in (3). Put
\(C_r(z)=U_r(z/2)\), \(r\ge0\). Laurent expansion after
\(z=w+w^{-1}\) proves the polynomial fusion identity
\[
 C_rC_s=\sum_{j=0}^{\min(r,s)}C_{r+s-2j}.
 \tag{18}
\]
For the basis products, \(r,s\le N-1\), so every index on the
right is at most \(2N-2\). For \(0\le v\le N-2\), another
Laurent identity gives
\[
 2T_N(z/2)C_v=C_{N+v}-C_{N-v-2}.
 \]
Using the full relation \(2T_N(z/2)=-2\), including multiplicities,
one obtains
\[
                    C_{N+v}=-2C_v+C_{N-v-2}
                           \quad\hbox{in }\mathcal H_N.
 \tag{19}
\]
Each unreduced term of (18) therefore has circle coefficient
mass at most three, and there are at most \(N\) such terms.
The signs in (2) do not affect this bound. It follows that
\[
 \|L_iL_j\|_\circ\le3N,\qquad
 \|fg\|_\circ\le3N\|f\|_\circ\|g\|_\circ,\qquad
 \|M_f\|_\circ\le3N\|f\|_\circ .
 \tag{20}
\]

F gives the original signed-power expansion, with its full
Hermite data and retained unit phase,
\[
 R^n=\kappa^n\sum_{j=1}^N\beta_{j-1}^{(n)}L_j,\qquad
 \sum_j|\beta_{j-1}^{(n)}|
                       \le2N(1+|n|/2).
 \tag{21}
\]
This bound is for every integer \(n\), positive, negative or zero;
it is not obtained from a semisimple evaluation of the crossing.
For clarity its finite Fourier input is the paired value/normal
data \(|h_k|=1\) and \(|d_k|\le |n|N/2\). Their exact alias inverse
gives first-kind coefficients \(|a_0|\le1\),
\(|a_j|\le1+|n|/2\). Taking the actual second-kind differences
\((-1)^j(a_j-a_{j+2})\), with \(a_N=a_{N+1}=0\), gives (21).

Let \(b_n=1+|n|/2\). Since \(|\kappa|=1\), (20)--(21) imply
\[
                    \|M_{R^{\pm n}}\|_\circ\le6N^2b_n.
 \tag{22}
\]
Combining this with (12)--(15) yields explicit uniform bounds
\[
 \boxed{\quad
 \|\widetilde K_n\|_\circ,\ \|P_n\|_\circ\le36N^4b_n^2,\qquad
 \|G_n\|_\circ\le18\pi N^5b_n^2,\qquad
 \|u_n\|_\circ\le6b_n .
 \quad}
 \tag{23}
\]
For fixed signed \(n\), the splitting is therefore polynomially
conditioned in this recorded physical circle norm. No inverse of
a confluent Vandermonde matrix or small Casimir-node separation
was estimated. Formula (19), rather than distinct-root reduction,
keeps the full normal directions.

## 5. A positive metric and coupled filling slots

Declare the basis (2) orthonormal and denote its Hilbert norm by
\(\|\cdot\|_2\). Pull this metric back by the actual multiplier:
\[
              \langle f,g\rangle_n
                   =\langle R^nf,R^ng\rangle_2 .
 \tag{24}
\]
Then \(\widetilde K_n\) is self-adjoint and nonnegative, with
the same eigenvalues (8). The projection \(P_n\) is orthogonal.
Its normalized vector is \(R^{-n}L_N\), and
\[
 |\phi_n(f)|=N^2\|P_nf\|_n,\qquad
 \|f-P_nf\|_n
            \le\frac{\pi N}{2}\|\widetilde K_nf\|_n .
 \tag{25}
\]
Both assertions follow by writing \(R^nf\) in the orthonormal
circle basis; no Cauchy equality for the exterior source is assumed.
Since \(\|v\|_2\le\|v\|_\circ\le\sqrt N\|v\|_2\), (22) gives
\[
 (6N^{5/2}b_n)^{-1}\|f\|_2
            \le\|f\|_n\le6N^{5/2}b_n\|f\|_2 .
 \tag{26}
\]
This is polynomial equivalence to the specified circle coefficient
metric, not to every physical tensor-space norm.

For \(r\) filling slots retain an arbitrary coupled class
\(H\in\mathcal H_N^{\otimes r}\) and signed powers \(n_1,\ldots,n_r\).
Use the tensor metric pulled back by \(\bigotimes_i M_{R^{n_i}}\).
Let \(P_i,K_i\) act as \(P_{n_i},\widetilde K_{n_i}\) in their
own slot, and put
\[
 P=\prod_iP_i,\qquad \phi_{\boldsymbol n}=\bigotimes_i\phi_{n_i}.
 \]
The \(P_i\) are commuting orthogonal projections. Expanding in the
tensor circle basis gives the pointwise indicator inequality
\(1-\prod_i p_i\le\sum_i(1-p_i)\), \(p_i\in\{0,1\}\), and hence
\[
 \boxed{\quad
 \|H-PH\|_{\boldsymbol n}^2
   \le\sum_i\|(I-P_i)H\|_{\boldsymbol n}^2
   \le\left(\frac{\pi N}{2}\right)^2
                     \sum_i\|K_iH\|_{\boldsymbol n}^2,\qquad
 |\phi_{\boldsymbol n}(H)|=N^{2r}\|PH\|_{\boldsymbol n}.
 \quad}
 \tag{27}
\]
No factorization of \(H\) was used. Thus, if the actual source
satisfies the additional estimate
\[
 \left(\frac{\pi N}{2}\right)^2
       \sum_i\|K_iH\|_{\boldsymbol n}^2
                         \le\delta^2\|H\|_{\boldsymbol n}^2,
 \qquad 0\le\delta<1,
 \]
orthogonality gives the exact consequence
\[
 |\phi_{\boldsymbol n}(H)|
       \ge N^{2r}\sqrt{1-\delta^2}\,\|H\|_{\boldsymbol n}.
 \tag{28}
\]
The source estimate in this implication is not proved here.
Polynomial conditioning and a one-dimensional period space do
not make it automatic. The metric in (24) is explicit and uses
only the chosen filling powers; an exterior source can have
a large component in the kernel of its original closing row.

## 6. Scope and coverage

The earlier Fourier--Hermite kernel and positive Gram already
give polynomial coordinate bounds for the original circle packet.
The additional statement here is the explicit singular
endomorphism (8), its crossing conjugate, and the exact
kernel/period splitting (14)--(17).

For \(n\ne0\), \(\widetilde K_n\) is not claimed equal to
\[
 \frac1{\sin t\,f_{N,n}(t)}
    \int_{-1/2}^{1/2}
       \sin(t+2\pi\rho/N)f_{N,n}(t+2\pi\rho/N)
             H(-2\cos(t+2\pi\rho/N))\,d\rho .
 \tag{29}
\]
Here \(f_{N,n}(t)=q^{nd^2/4}\exp(-nt^2/(2h))\),
\(h=2\pi i/N\), is the actual centered Gaussian lift of the
crossing values and normals. Formula (29) uses that lift
between nodes. In (13), \(R^nH\) is first its full quotient
class, whose canonical polynomial agrees with that lift only
in the required nodal jets. Averaging intermediate values need
not preserve that agreement. No equality of their principal
symbols or microlocal interpolation estimate is asserted.

Likewise a polynomial bound for \(G_n\) does not estimate
\(\phi_n(f)\) from below. Equation (16) records that unknown
coordinate exactly and allows it to vanish. The result applies
to the original class supplied by any exterior contraction,
but does not prove its overlap with the period line, select
a geometric component, or remove relative boundary currents.

## Complete proof-source pins

* N: papers/newton-calculus/finite.tex, SHA256
  2db2d7e15df0210c32bace4c761bdabadbb5d67140473a61425dac4d1e382f8e.
* F: notes/actual_twist_circle_fourier_kernel.md, SHA256
  1d93f6f13d271c56eee6e7ea8ddf5b9ea0eea92a2076ede7068df552bab94292.

N supplies the full physical algebra, circle basis, trace and
crossing normalization. F supplies the complete signed-power
coefficient bound. The average, fusion reduction, exact
splitting and induced norm estimates are proved here.
Only written mathematics and text/hash operations were used.
Frozen notes and public manuscripts are unchanged.
