# Positive Ward measure and the coherent Cauchy tail of an original turn

Private written proof, 17 November 2026.

The source-exact Ward representative has a positive Stieltjes density
on its actual spectral cut. The double physical rows are exactly
orthogonal for the resulting finite-moment measure. This identifies
the jump of a general turned source by an exact Plancherel formula.

More particularly, the difference between its canonical polynomial
and its Ward representative is one Cauchy transform. Orthogonality
turns its estimate into a sum of inverse physical rows. The estimate
applies to every actual input, including a product of received
sources followed by any original integer multiplication crossing.
No input first normal is estimated or discarded in this step.

This controls the coherent null correction, not the Ward
representative itself or a subsequent prescribed scalar.

## 1. Original source and one global Ward pair

Put
\[
 N\ge2,\quad D=N-1,\quad m=\lfloor N/2\rfloor,\quad
 \theta=\pi/N,\quad \eta=(-1)^D,
\]
\[
 c_j=2\cos((2j+1)\theta),\qquad
 P_N(C)=2T_N(C/2)+2,\qquad
 \mathcal A_N=\mathbb C[C]/(P_N).
 \tag{1}
\]
The double indices are \(0\le j<m\). At odd \(N=2m+1\),
the remaining simple node is \(c_*=-2\).
Write \(\theta_j=(2j+1)\theta\) and \(a_j=4-c_j^2\).
The original Newton data are
\[
 s_r=2\sin(r\theta),\quad S_r=\prod_{b=1}^r s_b,\quad
 e_r(C)=S_r^{-2}\prod_{a<r}(c_a-C),\quad
 K_N(w,C)=\sum_{r=0}^{D}e_r(w)e_r(C),
\]
with empty products equal to one.
The original normalization is
\[
 \phi_N(f)=\eta N^2[C^D]\operatorname{rem}_{P_N}f,\qquad
 Te_r=e_{D-r},
\]
\[
 F_j(C)=K_N(c_j,C),\qquad
 G_j(C)=\partial_wK_N(c_j,C).
 \tag{2}
\]
There is no \(G_*\). The pinned confluent source proves
\[
 TF_j=\delta_j=\frac{P_N(C)}{\eta N^2(C-c_j)},\quad
 \phi_N(\delta_j f)=f(c_j),\quad
 \phi_N(G_jF_k)=\frac{\eta}{a_j}\delta_{jk},
 \tag{3}
\]
for double \(j,k\), and \(T\) is a bilinear Frobenius isometry
and an involution.

Let \(\Omega=\mathbb C\setminus[2,\infty)\). The original even
Ward representative of \(G_0\) is denoted by \(\widetilde Q_N\).
With \(C=-2\cos t\) and \(|\Re t|<\pi\), it is
\[
 \widetilde Q_N(C)=-
 \frac{g_N'(D/2-t/(2\theta))-g_N'(0)}
                         {2\theta\sin\theta},
\]
\[
 g_N'(z)=\frac{\pi}{N^2}
       \sum_{r=0}^{D}(z-r)\cot\frac{\pi(z-r)}N .
 \tag{4}
\]
Evenness permits spectral descent through \(C=-2\).
This gives one holomorphic function on \(\Omega\), real on
\((-\infty,2)\), with \(\widetilde Q_N(c_0)=0\).
It has the full physical Hermite data of \(G_0\).

For \(j\ge1\) in the double range, retain the original
common-shift determinant and its derivative
\[
 F_j^\epsilon(C)=
 \frac{\det(\mathcal J_j(\epsilon)-CI)}
                         {\prod_{r<j} A(r+\epsilon)},\qquad
 R_j(C)=\partial_\epsilon F_j^\epsilon(C)|_{\epsilon=0},
 \qquad R_0=0,
\]
\[
 c'(j)=-4\theta\sin\theta_j,\qquad
 \widehat G_j(C)=
 \frac{c'(0)F_j(C)\widetilde Q_N(C)+R_j(C)}{c'(j)} .
 \tag{5}
\]
Here \(c_0\) is fixed during the common shift. The complete
normal-source theorem proves that \(\widehat G_j\) has the
original value and first inner normal of \(G_j\) at every
double physical node, and its value at the odd simple node.
For \(j=0\), (5) means \(\widehat G_0=\widetilde Q_N\).
At \(N=2\) this is the only normal row, so no nontrivial
common-shift determinant is needed.

For an arbitrary actual \(A\in\mathcal A_N\), put
\[
 H_A=\operatorname{can}(TA).
\]
Expanding its original input trace gives the exact ordinary
polynomial formula
\[
 H_A(C)=\eta\sum_{j<m}
 \{a_jA(c_j)G_j(C)+(a_jA'(c_j)-c_jA(c_j))F_j(C)\}
 +\mathbf1_{\mathrm{odd}}A(-2)F_*(C).
 \tag{6}
\]
Replace only \(G_j\) by (5), and define
\[
 \widehat H_A=Y_A+\widetilde Q_N L_A,
\qquad
 L_A=4\eta\sin\theta\sum_{j<m}\sin\theta_j A(c_j)F_j,
 \tag{7}
\]
\[
 Y_A=\eta\sum_{j<m}
 \left\{\frac{a_jA(c_j)}{c'(j)}R_j
                 +(a_jA'(c_j)-c_jA(c_j))F_j\right\}
 +\mathbf1_{\mathrm{odd}}A(-2)F_* .
 \tag{8}
\]
Thus \(\widehat H_A\) is source-equivalent to \(H_A\) with
all physical normals retained. Their difference divided by
\(P_N\) is holomorphic on \(\Omega\), including the physical
nodes. The polynomial degrees satisfy
\[
 \deg L_A\le m-1,\qquad
 \deg Y_A\le
 \begin{cases}m-1,&N=2m,\\m,&N=2m+1.\end{cases}
 \tag{9}
\]
The formulas hold with arbitrary ordinary free spectator
coefficients and may be differentiated in those coefficients.

## 2. The positive cut measure

For \(x>2\), set \(h(x)=\operatorname{arcosh}(x/2)>0\) and
\[
 \rho_N(x)=\frac{N}{4\pi\sin\theta}
                  \tanh\frac{Nh(x)}2,\qquad
 d\mu_N(x)=\frac{N^2\rho_N(x)}{P_N(x)}\,dx.
 \tag{10}
\]
This is a positive measure on \((2,\infty)\):
\[
 P_N(2\cosh h)=e^{Nh}(1+e^{-Nh})^2>0.
\]
Its moments through degree \(N-2\) are finite. Indeed
\(\rho_N(x)=O_N(\sqrt{x-2})\) at \(2\), while at infinity
\[
 \rho_N(x)=b_N+O_N(x^{-N}),\qquad
 b_N=\frac{N}{4\pi\sin\theta},\qquad P_N(x)\sim x^N.
 \tag{11}
\]
The moment of degree \(N-1\) diverges logarithmically.

**Theorem 1.** On the entire slit plane,
\[
 \boxed{\quad
 \widetilde Q_N(C)=\int_2^\infty \rho_N(x)
       \left(\frac1{x-C}-\frac1{x-c_0}\right)dx .
 \quad}
 \tag{12}
\]
In particular \(\widetilde Q_N\) has positive imaginary part
in the upper half-plane. For every polynomial \(f\) with
\(\deg f\le N-2\),
\[
 \boxed{\quad \phi_N(G_0f)=\eta\int_2^\infty f\,d\mu_N.\quad}
 \tag{13}
\]

**Proof.** The pinned Ward monodromy gives the exact
upper-minus-lower spectral jump
\[
 \widetilde Q_{N,+}(2\cosh h)
       -\widetilde Q_{N,-}(2\cosh h)
          =\frac{iN}{2\sin\theta}\tanh(Nh/2)
          =2\pi i\rho_N(2\cosh h).
 \tag{14}
\]
The integral in (12) converges normally on compact slit sets.
It has that same jump and vanishes at \(c_0\). At \(2\),
both functions are bounded. For the integral this follows
from the local square-root behavior of its density; for
the Ward function it follows from (4) at \(t=\pm\pi\).

For completeness the normalization at infinity does not
leave an unproved entire term. Use the branch with
\(|\Re t|\le\pi\), \(\Im t>0\) at large \(|C|\).
The finite cotangent sum in (4) gives
\[
 g_N'(D/2-t/(2\theta))
       =-it/2+O_N((1+|t|)e^{-\Im t}).
 \tag{15}
\]
Here \(\cot z=i+O(e^{2\Im z})\) in the lower half-plane,
and the centered finite sum of its linear factors is exact.
Since \(\log(-C)=-it+o(1)\) on this slit branch,
\(\widetilde Q_N(C)=-b_N\log(-C)+O_N(1)\).
The integral in (12) has \(O_N(1+\log|C|)\) growth:
split its density as \(b_N+(\rho_N-b_N)\), use
\[
 \int_2^\infty
       \left(\frac1{x-C}-\frac1{x-c_0}\right)dx
                 =\log\frac{2-c_0}{2-C},
\]
and the integrable \(O_N(x^{-N})\) tail in (11).
Its derivative is \(O_N(x^{-N-1})\) at infinity.
Thus the same bound holds up to either large cut bank:
split the tail integral into \(x<R/2\), \(R/2<x<3R/2\),
and \(x>3R/2\), and subtract its value at \(x=R\) in
the middle interval. The subtracted numerator is bounded
by \(O_N(R^{-N-1}|x-R|)\); the constant part has an
explicit logarithmic integral. These estimates also
bound the limiting principal values.
The difference therefore extends through the cut and its
endpoint to an entire function of logarithmic growth.
Cauchy's derivative estimate makes it constant, and its
value at \(c_0\) is zero. This proves (12).
The positive imaginary part follows directly from the
integrand, because the subtraction is real.

Apply a whole keyhole contour to
\(\widetilde Q_N(C)f(C)/P_N(C)\).
Its outer integral tends to zero: the integrand is
\(O_N(\log R/R^2)\) when \(\deg f\le N-2\).
The cap at \(2\) tends to zero as well.
The physical residues equal those of \(G_0f/P_N\),
including the double-node residues. With the upper bank
oriented from \(2\) to infinity, (14) gives
\[
 \sum_{\text{physical poles}}\operatorname{Res}
       \frac{\widetilde Q_N f}{P_N}
                  =\int_2^\infty \frac{\rho_N f}{P_N}\,dx.
 \tag{16}
\]
Multiplication by \(\eta N^2\) is the original closing,
which proves (13). No normal or endpoint pole has been
replaced by a distinct-value trace. \(\square\)

## 3. Exact physical-row orthogonality and jump Plancherel

**Theorem 2.** For the entire double-index range,
\[
 \boxed{\quad
 \int_2^\infty F_j(x)F_k(x)\,d\mu_N(x)
        =\frac{\delta_{jk}}{4\sin\theta\sin\theta_j}.
 \quad}
 \tag{17}
\]
Consequently
\[
 \boxed{\quad
 \int_2^\infty |L_A(x)|^2\,d\mu_N(x)
         =4\sin\theta\sum_{j<m}\sin\theta_j|A(c_j)|^2.
 \quad}
 \tag{18}
\]
Every \(F_j\) in (17) has simple roots in \((2,\infty)\).
The degree-zero row has no roots.

**Proof.** Use the whole keyhole for
\(\widehat G_j(C)F_k(C)/P_N(C)\). Its numerator has growth
at most \(O_N(C^{j+k}\log C)\), where \(j+k\le N-2\).
Thus the outer circle vanishes just as in (16).
Its jump is
\[
 2\pi i\rho_N(C)\frac{c'(0)}{c'(j)}F_j(C)F_k(C).
 \]
Source equivalence and (3) yield
\[
 \frac{\eta}{a_j}\delta_{jk}
   =\eta\frac{c'(0)}{c'(j)}
                         \int F_jF_k\,d\mu_N.
 \tag{19}
\]
Since \(a_j=4\sin^2\theta_j\) and
\(c'(0)/c'(j)=\sin\theta/\sin\theta_j\), this is (17).
All moments used are finite, also at \(N=2\).
Real coefficients and expansion of (7) give (18).

The rows \(F_0,\ldots,F_{j-1}\) span all polynomials of
degree below \(j\). Thus \(F_j\) is orthogonal to that
whole space for a strictly positive measure on
\((2,\infty)\). The usual sign-change proof is elementary
here: multiply \(F_j\) by the product of its roots where
its sign changes in this interval. If there were fewer
than \(j\) such roots, the resulting nonzero polynomial
would have one sign on the support, but zero integral
by orthogonality. This contradiction proves the root
assertion, including simplicity. \(\square\)

At odd \(N=2m+1\), the simple row \(F_*\) has degree \(m\).
Its squared norm for \(\mu_N\) diverges logarithmically;
it is deliberately absent from (17)--(18).
Its actual simple physical value is retained in \(Y_A\).
For \(N=2\), the family in (17) is just \(F_0=1\);
the formulas give \(\mu_N((2,\infty))=1/4\).
In general the mass is \(1/(4\sin^2\theta)\).

One exact closing interpretation of (18) is worth keeping.
If \(\deg B\le m-1\), the same whole contour gives
\[
 \phi_N((TA)B)=\eta\int_2^\infty L_A(x)B(x)\,d\mu_N(x).
 \tag{20}
\]
The degree bound ensures that \(Y_AB/P_N\) and
\(\widetilde Q_NL_AB/P_N\) have vanishing outer circles
at both parities. Thus this is the original closing
in its stated range, not a newly selected positive observation.

## 4. The coherent null tail and its inverse-row estimate

**Theorem 3.** For every actual \(A\in\mathcal A_N\),
\[
 \boxed{\quad
 \frac{\widehat H_A(C)-H_A(C)}{P_N(C)}
       =\frac1{N^2}\int_2^\infty
                         \frac{L_A(x)}{x-C}\,d\mu_N(x).
 \quad}
 \tag{21}
\]
The left side is interpreted by holomorphic continuation
at the physical nodes. On \(\Omega\), writing
\(d(C)=\operatorname{dist}(C,[2,\infty))>0\), one has
\[
 \boxed{\quad
 \left|\frac{\widehat H_A(C)-H_A(C)}{P_N(C)}\right|
     \le\frac1{N^2d(C)}
            \sum_{j<m}\frac{|A(c_j)|}{|F_j(C)|}.
 \quad}
 \tag{22}
\]
There is no input-normal term or odd-simple-value term
in this exact tail.

**Proof.** Set \(f=(\widehat H_A-H_A)/P_N\).
The full source equivalence removes all physical poles.
The function is bounded at \(2\), has jump
\[
 f_+-f_-=2\pi i\,\frac{\rho_N L_A}{P_N},
 \]
and tends to zero at infinity. More precisely (9)
and \(\deg H_A\le N-1\) give \(f=O_N(1/C)\),
with a smaller logarithmic contribution.
Its jump density is integrable at both ends of the cut.
The keyhole Cauchy formula for \(f(z)/(z-C)\) therefore
has no outer-circle or endpoint term and gives (21).
This proves its plus sign with the same upper-minus-lower
convention as (14).

For a double row put
\[
 S_j(C)=\int_2^\infty\frac{F_j(x)}{x-C}\,d\mu_N(x).
 \]
The polynomial
\((F_j(x)-F_j(C))/(x-C)\) has degree below \(j\).
Orthogonality consequently gives the exact identity
\[
 F_j(C)S_j(C)
          =\int_2^\infty\frac{F_j(x)^2}{x-C}\,d\mu_N(x).
 \tag{23}
\]
There is no zero of \(F_j(C)\) off the cut.
Positivity of the squared integrand's measure and (17)
now imply
\[
 |S_j(C)|\le
 \frac1{4\sin\theta\sin\theta_j\,d(C)\,|F_j(C)|}.
 \tag{24}
\]
Insert (7) into (21) and use (24). The normalization
factors cancel exactly, giving (22). \(\square\)

The estimate is for a coherent Cauchy tail. It does not
estimate \(Y_A\) and \(\widetilde Q_NL_A\) separately.
In particular (18) is compatible with those two channels
having large compensating values away from the grid.

There is also uniform control of fixed output derivatives.
For every compact \(K\Subset\Omega\) and fixed \(r\ge0\),
\[
 \left|\partial_C^r
       \frac{\widehat H_A-H_A}{P_N}(C)\right|
 \le C_{K,r}N^{r-2}
               \sum_{j<m}\frac{|A(c_j)|}{|F_j(C)|},
                  \qquad C\in K.
 \tag{25}
\]
Indeed all roots of \(F_j\) lie on the cut and \(j<N\).
On a disk of radius \(d(C)/(4N)\), each root factor
changes by a ratio between \(1-1/(4N)\) and
\(1+1/(4N)\). Hence \(F_j\) changes by bounded factors,
uniformly in \(j,N\). Apply (22) there and Cauchy's
estimate. Derivatives in any free spectator parameter
instead replace \(A(c_j)\) by its corresponding derivative,
by the exact linearity of (21).

## 5. Original composition and the retained closing

Let \(H_1,\ldots,H_s\in\mathcal A_N\) be any actual received
sources, with their full canonical jets, and let \(p\in\mathbb Z\).
Use the original input
\[
             A=\operatorname{can}\left(R^p\prod_{a=1}^sH_a\right).
 \tag{26}
\]
Every original physical crossing value has modulus one.
Therefore Theorem 3 gives directly
\[
 \left|\frac{\widehat H_A-T(R^p\prod_aH_a)}{P_N}(C)\right|
 \le\frac1{N^2d(C)}
             \sum_{j<m}\frac{\prod_a|H_a(c_j)|}{|F_j(C)|}.
 \tag{27}
\]
Here the turned expression means its canonical polynomial.
This estimate holds for every integer \(p\); no derivative
of the crossing is omitted from \(Y_A\).
Products and canonical reduction preserve the values used
on the right. All original normal data remain in the
exact representative (7)--(8) and its source equivalence.

For clarity, for arbitrary \(A,B\in\mathcal A_N\), the full
two-source Frobenius pairing also has an exact cut formula. Put
\[
 Q_{\mathrm R}(x)=\frac{\widetilde Q_{N,+}(x)
                          +\widetilde Q_{N,-}(x)}2.
 \]
Schwarz reflection makes this real. The whole keyhole gives
\[
 \begin{split}
 \phi_N((TA)(TB))={}&
       \mathbf1_{\mathrm{odd}}A(-2)B(-2)\\
 &+\eta\int_2^\infty
       \{Y_AL_B+L_AY_B+2Q_{\mathrm R}L_AL_B\}\,d\mu_N .
 \end{split}
 \tag{28}
\]
Every cut term converges. At even levels the outer circle
vanishes. At odd \(N=2m+1\), only the product of the leading
\(Y\) coefficients contributes. Indeed
\(F_*=K_N(-2,C)\) has leading coefficient \((-1)^m/N\):
\(e_m(-2)=1\) because \(c_a+2=s_{m-a}^2\) for \(a<m\),
and \(S_m^2=N\). Thus the outer coefficient is
\(A(-2)B(-2)/N^2\), giving the displayed simple term.
The jump of the product is precisely the integrand in
(28) times \(2\pi i\rho_N\), which fixes its sign.

The cut pairing on \((Y,L)\) has matrix
\[
             \begin{pmatrix}0&1\\1&2Q_{\mathrm R}\end{pmatrix}
 \]
and determinant \(-1\). It therefore retains the
indefinite original Frobenius closing, rather than turning
that closing into the positive jump norm (18).
No conclusion here bounds \(\widehat H_A\) on a parent
contour, pays the right side of (27) by a prescribed joint
action, or proves a nonzero coefficient after another
shared trace. Those remain distinct source estimates.

## 6. Complete direct sources

All three entire direct texts were read and their used
implications checked at these pins:

* [Odd Ward logarithmic factorial](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_odd_ward_logarithmic_factorial.md),
  SHA256 63ae4693846f00a9b843b98b423959964a8ccb3a72dc8ee0fc1ac36b69f3d4b8:
  finite cotangent formula, even full-jet representative,
  its normalization, poles and angular monodromy.
* [Coherent full-normal physical products](research_physical_products_full_normal_coherent_contour.md),
  SHA256 2f150a6d5a901521637f67c6db8fac96c6c6a14a0b23546e8383d1565189d574:
  exact common-shift normal representative, polynomial
  remainder, upper-minus-lower Ward cut and original
  contour orientation.
* [Confluent row closing](research_confluent_row_closing_and_positive_quotient.md),
  SHA256 daf5760f74dbd9d9c9646a1a18b95cdffc1f42ebc3cbcfc0a1b9f79b2ad77251:
  full original trace, reproducing rows, degrees,
  Frobenius pairing, signed crossing values and normals.

Only written mathematics, source-text reads and metadata
hashes were used. No mathematical program, numerical
experiment, test, build or compilation was run.
Frozen source notes and public manuscripts are unchanged.
