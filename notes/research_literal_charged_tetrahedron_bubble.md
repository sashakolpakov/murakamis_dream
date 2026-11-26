# The literal charged tetrahedron inverse and three-face bubble

Private written proof, 17 November 2026. We reconstruct the inversion
and bubble in Kashaev's 1994 definitions [K], including their finite
normalization sums. Neither the printed inversion identity nor CG
duality is used as a proof premise. This is the charged face-state
identity at odd level, not yet the original marked-source adapter
for deleting a free vertex.

## 1. The specified functions and regular data

Let \(N>2\) be odd, \(\omega\) a primitive \(N\)-th root, and interpret
\(1/2\) modulo \(N\), as in [K]. All finite indices are in
\(\mathbb Z/N\mathbb Z\). Choose nonzero roots

\[
 P=x_p,\quad Q=x_q,\quad R=x_r,\quad
 B=x_{pq},\quad C=x_{qr},\quad H=x_{pqr},
\]
\[
 B^N=P^N+Q^N,\qquad C^N=Q^N+R^N,\qquad
 H^N=P^N+Q^N+R^N.                                      \tag{1}
\]

Thus the three individual central parameters and all the partial
sums displayed in (1) are nonzero. We work on a lifted regular
parameter domain with fixed choices of these roots. Put

\[
 \langle U,V\rangle=\frac{U^N-V^N}{N(U-V)},\qquad
 \langle U\rangle=U^{N-1},
\]
\[
 \kappa_*=
 \frac{\langle B,Q\rangle^{1/2}\langle H,R\rangle^{1/2}
                         \langle C,R\rangle^{1/2}}
      {\langle H,C\rangle^{1/2}}.                       \tag{2}
\]

The same square-root choices in (2) are used in both normalizations
below. None of its brackets vanishes under (1). Independently changing
the sign of only one normalization is not permitted.

For \(x^N+y^N=z^N\) with \(xyz\ne0\), define the periodic sequence

\[
 W(x,y,z;k)=\prod_{j=1}^{[k]}\frac{y}{z-x\omega^j},
 \qquad
 w(x,y,z;i,j)=W(x,y,z;i-j)\omega^{j^2/2}.               \tag{3}
\]

The cyclic product is one, so the recurrence extends (3) consistently
to every integer. Also write

\[
 v(u;k)=\prod_{j=1}^{k}(1-u\omega^j)^{-1}\quad(0\le k<N),\qquad
 f(u,v\mid z)=\sum_{k=0}^{N-1}\frac{v(u;k)}{v(v;k)}z^k,
 \qquad z^N=\frac{1-u^N}{1-v^N}.                       \tag{4}
\]

In (4) the letter \(v\) inside \(f\) is a parameter; \(v(u;k)\) is
the displayed one-argument product. Extend that product to all integers
by \(v(u;k+1)=v(u;k)/(1-u\omega^{k+1})\). Then
\(v(u;k+N)=v(u;k)/(1-u^N)\); the summand in (4), rather than
either product separately, is cyclic.

Set

\[
 u=\frac RH,\quad v=\frac{R}{\omega C},\quad
 z=\frac{BC}{HQ},\qquad
 \rho=\kappa_* f(u,v\mid z),\qquad
 \bar\rho=\kappa_* f(\omega v,u/\omega\mid z^{-1}).     \tag{5}
\]

These are exactly [K, (1.25),(1.29)], including the three numerator
square roots in (2). The bar is a label, not complex conjugation.
The literal two matrices are [K, (1.24),(1.28)]:

\[
 \mathcal R^{\gamma,\delta}_{\alpha,\beta}
 =\frac{\rho}{C^{N-1}}\,
   \omega^{\alpha\delta}
   w(HQ,PR,BC;\gamma,\alpha)\,
   \delta_{\beta,\gamma+\delta},
\]
\[
 \overline{\mathcal R}^{\alpha,\beta}_{\gamma,\delta}
 =\frac{\bar\rho}{B^{N-1}}\,
   \frac{\delta_{\beta,\gamma+\delta}}
        {\omega^{\alpha\delta}
           w(HQ/\omega,PR,BC;\gamma,\alpha)}.          \tag{6}
\]

Every denominator in these finite definitions is nonzero on (1).
The apparently additional denominators used in the calculations
below are nonzero there as well: in particular
\((HQ)^N-(BC)^N=-P^NR^N\), and \(H^N-C^N=P^N\).

## 2. The complete finite normalization product

We prove the identity needed for (5) without importing a transformation
formula for \(f\). Temporarily use arbitrary regular \(u,v,z\) satisfying
(4), and put

\[
 a_k=\frac{v(u;k)}{v(v;k)}z^k,\qquad
 b_k=\frac{v(\omega v;k)}{v(u/\omega;k)}z^{-k},\qquad
 C_0=(1-\omega v)(1-u).
\]

The two sequences are periodic. Direct cancellation of their products
gives, including the cyclic seam,

\[
 b_k=\frac{g_k}{a_k},\qquad
 g_k=\frac{C_0}{(1-v\omega^{k+1})(1-u\omega^k)}.        \tag{7}
\]

Regroup the product of their two sums by \(n=j-k\). For
\(1\le n<N\), their recurrence gives

\[
 \frac{a_{k+n}}{a_k}g_k
 =C_0z^n
   \frac{\prod_{j=2}^{n}(1-v\omega^{k+j})}
        {\prod_{j=0}^{n}(1-u\omega^{k+j})}.            \tag{8}
\]

Multiply numerator and denominator by
\(\prod_{j=n+1}^{N-1}(1-u\omega^{k+j})\). The denominator becomes
\(1-u^N\). The numerator is a polynomial in \(\omega^k\) of degree
\(N-2\), with constant coefficient one. Summing over \(k\) kills
every nonconstant monomial. Thus

\[
 \sum_k\frac{a_{k+n}}{a_k}g_k
        =\frac{NC_0z^n}{1-u^N}\qquad(1\le n<N).       \tag{9}
\]

For \(n=0\), partial fractions and the finite geometric-root sum give

\[
 \sum_k g_k
 =\frac{NC_0}{\omega v-u}
       \left(\frac{\omega v}{1-v^N}
                       -\frac{u}{1-u^N}\right).      \tag{10}
\]

Here
\(\sum_k(1-t\omega^k)^{-1}=N/(1-t^N)\), obtained by
multiplying by \(1-t^N\) and summing the finite geometric series.
Combining (9),(10), and using (4), proves

\[
\begin{split}
 f(u,v\mid z)f(\omega v,u/\omega\mid z^{-1})
 &=\frac{NC_0}{1-u^N}
   \left\{\frac{\omega v z^N-u}{\omega v-u}
                        +\frac{z-z^N}{1-z}\right\}\\
 &=\frac{N(1-\omega v)(1-u)(1-z^N)(\omega vz-u)}
          {(1-u^N)(1-z)(\omega v-u)}.                 \tag{11}
\end{split}
\]

This proof first uses the displayed nonzero denominators; the
identity also extends wherever its literal finite sides are regular.
No such extension is needed for the parameters in (5).

For those parameters, substitution of (1) gives explicitly

\[
 \kappa_*^2=
 \frac{B^NQ^N(H-C)}
      {N^2(B-Q)(H-R)(C-R)},
\]
\[
 f(u,v\mid z)f(\omega v,u/\omega\mid z^{-1})
 =
 -\frac{NP^NR^N(C-R)(H-R)(B-Q)}
 {B^NQ^N(HQ-BC)(H-C)}.
\]

Consequently the full normalization, including its sign, is

\[
                   \rho\bar\rho
          =\frac{(PR)^N}{N(BC-HQ)}.                  \tag{12}
\]

## 3. Raw \(w\) orthogonality and the actual inverse

We now multiply the two matrices (6). Their Kronecker symbols first
give \(\beta=\beta'\). In
\((\overline{\mathcal R}\mathcal R)^{\alpha,\beta}
                                      _{\alpha',\beta'}\),
put \(n=[\alpha'-\alpha]\), \(k=\gamma-\alpha\), and, for this
calculation only, \(x=HQ,y=PR,z=BC\). Apart from an index-dependent
phase independent of \(k\), the remaining sum is

\[
 \sum_{k=0}^{N-1}\omega^{-nk}
        \frac{W(x,y,z;k-n)}{W(x/\omega,y,z;k)}.        \tag{13}
\]

For \(1\le n<N\), the ratio in (13) is exactly

\[
 \frac{z-x}{y^n}\prod_{j=1}^{n-1}(z-x\omega^{k-j}).    \tag{14}
\]

It is a polynomial in \(\omega^k\) of degree \(n-1\). After the
factor \(\omega^{-nk}\), none of its powers is divisible by \(N\);
hence (13) is zero. For \(n=0\), the ratio is
\((z-x)/(z-x\omega^k)\), so (13) equals

\[
                  \frac{Nz^{N-1}(z-x)}{y^N}.         \tag{15}
\]

The phase omitted in describing (13) is one when \(n=0\).
Multiplying (15) by the prefactor
\(\rho\bar\rho/(B^{N-1}C^{N-1})\), and using (12), gives one.
Thus

\[
       \overline{\mathcal R}\mathcal R=I,\qquad
       \mathcal R\overline{\mathcal R}=I.             \tag{16}
\]

The second equality follows because the matrices are finite square
matrices. This establishes the actual inverse with its primary
normalization, rather than naming a matrix “dual” and assuming (16).

## 4. Charged tensors, the face contraction, and the third trace

On the face-index space let
\(Z|j\rangle=\omega^j|j\rangle\),
\(X|j\rangle=|j+1\rangle\), and
\(Y=\omega^{1/2}XZ\). In the same branches as above, the primary
charged tensor and its opposite-orientation tensor are

\[
 T(a,c)=
 \omega^{ac/2}C^{N-1}
       Y_1^{-a}Z_1^{-c}\mathcal R Z_1^cZ_2^{-a},
\]
\[
 \bar T(a,c)=
 \omega^{-ac/2}B^{N-1}
       Z_2^{-a}Z_1^c\overline{\mathcal R}Z_1^{-c}Y_1^{-a}.
                                                               \tag{17}
\]

The first line is [K, (3.1)]. To check the second against the
conjugation definition (3.2), let \(\mathsf C|j\rangle=|-j\rangle\).
Then \(\mathsf C Z\mathsf C=Z^{-1}\) and
\(\mathsf C Y\mathsf C=Y^{-1}\). Conjugating the finite product at
indices \((-i,-j)\) changes \(w(x,y,z;-i,-j)\) to
\(1/w(x/\omega,y,z;i,j)\), with the roots of the conjugate parameters
chosen compatibly. For its scalar, replacing \(k\) by \(-k\) in
the periodic summand gives

\[
 f_{\omega^{-1}}(u,v\mid z)
             =f_\omega(v/\omega,u/\omega\mid z^{-1}).
\]

Applied to (5) with the conjugated root of unity, this is precisely
\(\bar\rho\). The same square-root choices are continued from a
compatible real parameter anchor. These finite identities give
(17), including its scalar \(B^{N-1}\), from the primary definition.
They do not choose independent normalization roots after contraction.

Write the tetrahedral edge charges as \(c_{ij}\). The four vertex
sums \(1/2\) imply

\[
 c_{01}=c_{23}=a,\qquad c_{12}=c_{03}=c,\qquad
 c_{02}=c_{13}=\tfrac12-a-c.                           \tag{18}
\]

Since \(N\) is odd these deductions and halves are legitimate.
The primary inverse-pair conditions are

\[
                  c_{13}+c'_{13}=1,\qquad
                  c_{01}+c'_{01}=0.
\]

By (18) they are exactly \(a'=-a,c'=-c\). Now (17),(16) cancel
without commuting any unpaired clock past a shear:

\[
 T(a,c)\bar T(-a,-c)
       =B^{N-1}C^{N-1}I
       =\langle s_{02}\rangle\langle s_{13}\rangle I. \tag{19}
\]

The reverse product has the same value. In the primary face
ordering, the inputs are \((\alpha_3,\alpha_1)\), and the outputs
are \((\alpha_2,\alpha_0)\). Thus gluing faces \(0,2\) is exactly
(19), leaving identity factors on faces \(1,3\). Gluing the two
copies of face \(1\) is the ordinary coordinate pairing
\(\delta_{\alpha_1,\alpha'_1}\). Its partial trace is therefore

\[
 \sum_{\alpha_0,\alpha_1,\alpha_2}T_u(s,c,\alpha)
              \bar T_u(s,c',\alpha')
 =N\langle s_{13}\rangle\langle s_{02}\rangle
                          \delta_{\alpha_3,\alpha'_3}.           \tag{20}
\]

There is no additional pivot in this **face-index** trace.
This is a conclusion from the literal charges and matrices,
not an assertion about a physical quantum-group cap.

## 5. The retained edge weights and the marked-link route

The three glued faces in (20) meet at vertex \(3\). Equation (18)
gives total charges

\[
 c_{03}+c'_{03}=0,\qquad
 c_{23}+c'_{23}=0,\qquad
 c_{13}+c'_{13}=1.
\]

Thus the charged-link rule in [K, (4.3)] routes the link through
\(0\!-\!3\!-\!2\); it does not erase an unmarked isolated vertex.
For the corresponding link move, the boundary edge \(02\) is
required to be initially non-link, and the detour is replaced by
\(0\!-\!2\). This is a boundary routing condition, not a conclusion
from local charges in an arbitrary exterior. The removed internal
non-link edge \(13\) has weight \(\langle s_{13}\rangle^{-1}\).
The local total on \(02\) is one before removal, so its exterior
charge is zero and it becomes a link edge afterwards; its old
non-link weight is \(\langle s_{02}\rangle^{-1}\).
These two factors cancel the decoration factors in (20).
The factor \(N\) is then canceled by
the relative vertex measure: the primary normalization \(N^{2-K}\)
has one extra factor \(N^{-1}\) before removal of this vertex.
All other boundary data are retained.

Accordingly the normalized local identity is valid with arbitrary
exterior tensors under exactly this routing and these charge data.
It can be differentiated in regular continuous decoration parameters
while retaining the displayed factors. This does not differentiate
the level off its root or specify an original meridian-normal family.

## 6. Scope and proof inputs

This reconstructs the primary charged face-state bubble by finite
algebra. It proves neither that the original \(P,S\) free vertices
already carry the required charged link detours nor that their local
tetrahedra have this face-module assignment.

In particular, a physical wire represented by a *pair* of face
indices is not the single face traced in (20). The original marked
quantum-group cap, its pivot and its cut matrix cannot be inserted
or removed by reinterpreting that trace. A global adapter must
transport the actual boundary state, all charge and root data,
and the retained source currents. Singular decoration limits are
not covered by the regular calculation above.

The sole direct source is R. M. Kashaev,
*Quantum Dilogarithm as a 6j-Symbol*,
[hep-th/9411147v2](https://arxiv.org/pdf/hep-th/9411147v2).
The entire 13-page paper was freshly read. Only its explicit finite
definitions and stated charge/edge-weight conventions are proof
inputs; its pentagon, inversion, bubble, and global invariance
assertions are not assumed. Equations (1.25),(1.29) were also
checked in rendered pages to retain their fraction layout.

Local archived PDF:
[research_archive/literal-charged-bubble-2026-11-17/kashaev1994.pdf](../research_archive/literal-charged-bubble-2026-11-17/kashaev1994.pdf).

SHA-256:
\(\texttt{dec5ba817a401b1ab88c6db1fbac6b8062c2cea05f19077097de247eca2642bb}\).

No mathematical programs or numerical experiments were used.
PDF extraction/rendering served only to read the primary definitions.

