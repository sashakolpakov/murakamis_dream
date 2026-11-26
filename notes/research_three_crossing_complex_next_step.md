# The actual next-crossing column on its geometric complex clock

Research note, 3 November 2026.

The ordinary clock polynomial of the original column
\(\gamma=MJM^3\mathbf e_0\) admits a nonzero complex asymptotic
near the clock needed by the adjacent three-crossing source.
The proof uses an exact finite transform of the original input.
Its exact scalar factorial part becomes a one-variable sum; its
entire remaining current is polynomially bounded on the clock
domain. The sum has a single principal saddle, with all finite
residue corrections retained.

The scalar enclosures in Section 5 are proved by exact rational
outward arithmetic. No free-boundary theorem for the complete
adjacent pair is claimed in this note.

## 1. The original polynomial and its prepared input

Use \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\),
\(\kappa=e^{\pi iD^2/(2N)}\), and
\[
 F_k=(Q;Q)_k,\qquad
 S_k=\prod_{r=1}^k2\sin(\pi r/N),\qquad
 \alpha=M^3\mathbf e_0,\qquad h_j=q^{j(j+2)}S_j^2.
 \tag{1}
\]
All powers use these fixed exponentials. Let \(A_N\) be the
exact partial reciprocal-factorial sum at a maximum of \(S_j^2\),
as in [the next-step theorem](research_three_crossing_next_step_profile.md).
That theorem proves, through both parities,
\[
 \alpha=\kappa^3A_Nh+\delta_N,\qquad
 \max_j|\delta_{N,j}|=O(N),\qquad
 A_N=N^{-1/2}\omega_N(1+O(N^{-1})),
 \quad
 \omega_N=e^{i\pi(1/4+1/(4N)-N/12)}.
 \tag{2}
\]
For an arbitrary original coefficient column \(u\), define
\[
 \mathcal G_u(X)=\frac1{N\kappa}
   \sum_{k=0}^{D}\frac{q^{k^2}u_{D-k}}{F_k}
       X^{D-k}\prod_{r=0}^{k-1}(X-Q^{-r}).
 \tag{3}
\]
This polynomial has degree at most \(D\), and
\[
 (MJu)_j=N\kappa^2(-q^{-1})^j\mathcal G_u(Q^{-j}).
 \tag{4}
\]
Both facts, with the original scalar and every color retained,
are proved in
[the lower half-disk error theorem](research_next_crossing_lower_half_disk_error.md).
Write \(G_N=\mathcal G_\alpha\).

**Lemma 1.** The prepared part of this actual polynomial is exactly
\[
 \boxed{\quad
 G_N(X)=A_NN
  \sum_{k=0}^{N-1}
       \frac{X^{D-k}Q^{k(k+1)}(X;Q)_k}{F_k^3}
          +\mathcal G_{\delta_N}(X).
 \quad}
 \tag{5}
\]
On every compact subset of
\[
                   0<|X|<13/20,\qquad \operatorname{Im}X<0,
 \tag{6}
\]
the second term and each of its fixed complex derivatives are
bounded by a polynomial in \(N\).

*Proof.* In (3) use
\[
 \prod_{r<k}(X-Q^{-r})
       =(-1)^kq^{-k(k-1)}(X;Q)_k,\qquad
 S_{D-k}S_k=N,\qquad
 F_k=(-i)^kq^{k(k+1)/2}S_k.
 \tag{7}
\]
The coefficient of the prepared vector \(\kappa^3A_Nh\)
simplifies to the summand in (5); its constant is one because
\((-1)^N\kappa^2q^{-1}=1\).
The polynomial bound is Corollary 2 of the cited error theorem
applied to (2), including its derivative assertion. \(\square\)

## 2. A holomorphic interpolation of the complete numerator product

For \(X\) in a compact subset of \(|X|<1\), and \(z\) in a
fixed rectangle on which \(|Xe^{2\pi iz}|<1\), define
\[
 \begin{split}
 \mathcal P_N(z;X)=\exp\left\{
 z\operatorname{Log}(1-X^N)
 -\sum_{\substack{m\ge1\\N\nmid m}}
 \frac{X^m(1-e^{2\pi imz})}{m(1-e^{2\pi im/N})}
                         \right\}.
 \end{split}
 \tag{8}
\]
The logarithms start at \(X=0\). The series is locally normally
convergent in the stated domain. Its factors with \(N\mid m\)
have not been discarded: their exact contribution is the
displayed \(z\operatorname{Log}(1-X^N)\).

**Lemma 2.** At every original index \(0\le k<N\),
\[
                 \mathcal P_N(k/N;X)=(X;Q)_k.                    \tag{9}
\]
On a closed rectangle satisfying the strict domain conditions
above, uniformly in \(z,X\),
\[
 \mathcal P_N(z;X)=
 \sqrt{\frac{1-X}{1-Xe^{2\pi iz}}}\,
 \exp\left(N\int_0^z\operatorname{Log}
                      (1-Xe^{2\pi it})\,dt\right)
                         (1+O(N^{-1})).
 \tag{10}
\]
The error is holomorphic, with the same order for fixed
derivatives on smaller sets.

*Proof.* Expand each logarithm in the finite product
\(\prod_{r=0}^{k-1}(1-XQ^r)\). For \(N\nmid m\), the
inner geometric sum is \((1-Q^{mk})/(1-Q^m)\). For \(m=N\ell\)
it is \(k\), whose total contribution is
\((k/N)\operatorname{Log}(1-X^N)\). This proves (9).

For \(1\le m<N/2\),
\[
 \frac1{1-e^{2\pi im/N}}
       =\frac{iN}{2\pi m}+\frac12+O(m/N).                       \tag{11}
\]
Substitution in (8) gives the integral and half-endpoint
factor in (10), with logarithmic error \(O(N^{-1})\).
Indeed all the resulting geometric power series have ratio
bounded strictly below one, uniformly on the prescribed set.
For \(m\ge N/2\), \(N\nmid m\), the reciprocal denominator
is at most \(C N\); these tails are exponentially small.
The omitted multiples and the explicit central term in (8)
are exponentially small as well, but were retained before
this estimate. Differentiating any fixed number of times
only inserts fixed powers of \(m\), so the same reasoning
proves the derivative version. \(\square\)

Put
\[
 \begin{split}
 \mathcal J(z)&=\int_0^z\operatorname{Log}(2\sin\pi t)\,dt,\\
 \Phi(z;X)&=(1-z)\operatorname{Log}X
    +\int_0^z\operatorname{Log}(1-Xe^{2\pi it})\,dt
    -3\mathcal J(z)+\frac{i\pi}{2}(z^2-z),\\
 b(z;X)&=
 \frac{e^{i\pi z/2}}{X(2\sin\pi z)^{3/2}}
                \sqrt{\frac{1-X}{1-Xe^{2\pi iz}}}.
 \end{split}                                                     \tag{12}
\]
The factorial logarithm is continued from \(0<z<1\).
The clock logarithm used below has argument in \((-\pi,0)\);
the other square roots are obtained from their displayed
zero-free factors.

Let \(\mathfrak G_N\) denote the canonical sine-factorial
interpolation, with \(\mathfrak G_N(k)=S_k\), from the
[factorial interpolation proof](research_uniform_factorial_and_boundary_decay.md).
The exact summand interpolation for the sum in (5) is
\[
 f_N(z;X)=
 X^{-1}e^{N(1-z)\operatorname{Log}X}
 e^{i\pi N(z^2-z)/2+i\pi z/2}
               \frac{\mathcal P_N(z;X)}{\mathfrak G_N(Nz)^3}.
 \tag{13}
\]
At \(z=k/N\), it equals
\(X^{D-k}Q^{k(k+1)}(X;Q)_k/F_k^3\), with no scalar adjustment.
On every compact bulk rectangle under consideration,
\[
 f_N(z;X)=N^{-3/2}b(z;X)e^{N\Phi(z;X)}(1+O(N^{-1})).
 \tag{14}
\]
This uses
\(\mathfrak G_N(Nz)=(2N\sin\pi z)^{1/2}
e^{N\mathcal J(z)}(1+O(N^{-1}))\).

## 3. The selected saddle and all real tails

Let \(\tau\) be the conjugate of the selected negative-source
root in
[the marked geometric branch](research_three_crossing_pendant_geometric_branch.md):
\[
 (\tau-2)^2(\tau^2-2\tau+2)=-2i,\qquad
 \tau\ \hbox{near }0.944-1.303i .
 \tag{15}
\]
Define
\[
 X_*=\frac1{\tau^2-3\tau+3},\qquad
 Y_*=\frac1\tau,\qquad
 z_*=\frac{\operatorname{Log}Y_*}{2\pi i},
 \qquad H=\operatorname{Im}z_* .
 \tag{16}
\]
The logarithm of \(Y_*\) has argument in \((0,\pi)\).
Exponentiating the stationary equation gives
\[
 e^{\Phi_z}
       =\frac{Y^2(1-XY)}{X(1-Y)^3},\qquad Y=e^{2\pi iz},
 \tag{17}
\]
so the equation is the quadratic
\[
                 (1-3X)Y^2+3XY-X=0.                            \tag{18}
\]
At \(X_*\), its two roots are \(1/\tau\) and \(1/(3-\tau)\).
The former has \(\Phi_z(z_*;X_*)=0\) on the specified
logarithmic branch. The other is not silently included in
this principal stationary equation.

Here and below take
\[
        \alpha=1/100,\qquad \beta=3/10,\qquad K=7/100.             \tag{19}
\]
The scalar bounds in Section 5 give
\[
 \begin{gathered}
 31/50<|X_*|<16/25,\qquad -2<\arg X_*<-39/20,\\
 7/50<\operatorname{Re}z_*<4/25,\qquad
 3/40<H<19/250,\\
 M:=\operatorname{Re}\Phi(z_*;X_*)>1/20,\qquad
              \operatorname{Re}\Phi(\beta;X_*)<0 .
 \end{gathered}                                                   \tag{20}
\]
These bounds also fix the full logarithmic charge.
At the selected point, both
\(\operatorname{Log}(1-X_*Y_*)\) and
\(\operatorname{Log}(2\sin\pi z_*)\) have arguments in
\((0,\pi/2)\). Substitution in
\[
 \Phi_z=-\operatorname{Log}X+\operatorname{Log}(1-XY)
         -3\operatorname{Log}(2\sin\pi z)+i\pi(z-1/2)
\]
puts its imaginary part strictly between \(-2\pi\) and \(2\pi\).
Equation (18) makes its exponential one, so the gradient is zero
without an additional integer charge.

The lower half-disk theorem gives, for every real \(s\in[0,1]\),
\[
 \operatorname{Re}\Phi(s;X)
              =T(s;X)-2\mathcal J(s),\qquad T(s;X)\le0.          \tag{21}
\]
Consequently every original summand with \(k/N\ge1/2\)
has rate at most zero. This assertion uses the finite-product
upper bounds, not an interpolation beyond its bulk strip.

For \(\beta\le s\le1/2\),
\[
 \partial_s\operatorname{Re}\Phi(s;X)
       =\log\frac{|1-Xe^{2\pi is}|}
                       {|X|(2\sin\pi s)^3}<0.                  \tag{22}
\]
Indeed the numerator is at most \(41/25\), whereas the
denominator is greater than \((31/50)(8/5)^3>41/25\).
Together with (20), this controls the other upper real tail.

For \(0\le s\le\alpha\), the inequalities
\(\sin\pi s\ge2s\), \(|X|\le16/25\) give
\[
 \operatorname{Re}\Phi(s;X)
 \le (1-s)\log(16/25)+s\log(41/25)
                              -3s(\log(4s)-1).                 \tag{23}
\]
The right side increases on this interval and is less than
\(-1/5\) at \(s=1/100\). For example use
\(\log(16/25)<-2/5\), \(\log(41/25)<1\), and \(\log25<4\).
Thus both omitted real tails have a strict gap below \(M\).
Uniform sine-factorial and smooth product estimates turn these
rate bounds into a polynomial prefactor times their exponent.
They include every original index and both parities.

## 4. A complete one-variable residue contour

For \(z=x+iy\) in the rectangle
\[
        \alpha\le x\le\beta,\qquad -K\le y\le H,
 \tag{24}
\]
one has \(|Xe^{2\pi iz}|<1\). In fact
\((16/25)e^{7\pi/50}<1\); the elementary bound follows from
\(\pi<22/7\) and \(e^{11/25}<25/16\).
Thus (8), (13), and (14) are valid throughout this entire
rectangle, including the lower contour.

The second derivative is
\[
 \Phi_{zz}
 =-\frac{2\pi iXe^{2\pi iz}}{1-Xe^{2\pi iz}}
                         -3\pi\cot\pi z+i\pi .                  \tag{25}
\]
Throughout (24), \(-\pi<\arg X+2\pi x<0\). Therefore
\[
 \operatorname{Re}\Phi_{zz}
   =\frac{2\pi\operatorname{Im}(Xe^{2\pi iz})}
                   {|1-Xe^{2\pi iz}|^2}
        -3\pi\operatorname{Re}\cot\pi z<0.                      \tag{26}
\]
The real part is strictly concave on every horizontal line,
and strictly convex on every vertical line.
At height \(H\) its unique maximum is \(M\), at \(z_*\).
The Hessian there is nonzero.

The lower horizontal correction also has a strict gap.
For \(0\le y\le K\), the logarithm
\(\operatorname{Log}(1-Xe^{2\pi i(x+iy)})\), and its
counterpart below the axis, have imaginary part in \((0,\pi/2)\).
Integrating the vertical derivative of the numerator integral
in (12), and using the reflection of \(\mathcal J\), gives
\[
 \operatorname{Re}\Phi(x-iK;X)
       -\operatorname{Re}\Phi(x+iK;X)
                \le2K(|\arg X|+\pi x).                         \tag{27}
\]
The quadratic contribution to this difference is
\(-\pi K+2\pi Kx\); the numerator integral contributes at most
\(\pi K\), and the clock logarithm contributes
\(-2K\arg X\). These are all the terms in (27).

By (21) and the exact crossing entropy bound
\(c=2\mathcal J(5/6)<1/3\),
\(\operatorname{Re}\Phi(x;X)\le c\) on the real interval.
Vertical convexity and \(K<H\) imply
\[
 \operatorname{Re}\Phi(x+iK;X)
      \le(1-K/H)c+(K/H)M
      \le M+\frac{17}{760}.                                    \tag{28}
\]
Here \(1-K/H<3/38\) and \(c-M<1/3-1/20=17/60\).
Combining (27)--(28) with the lower Fourier penalty gives
\[
 \operatorname{Re}\Phi(x-iK;X)-2\pi K
  \le M+\frac{17}{760}-K(7\pi/5-4)
                          <M-\frac1{200}.                     \tag{29}
\]
The last rational comparison follows already from
\(\pi>157/50\). The upper Fourier correction loses \(2\pi H\).

Move \(\alpha,\beta\) by \(O(N^{-1})\) to half-grid points.
The exact asymmetric upper-base residue identity is
\[
 \begin{split}
 \sum_{\alpha_N<k/N<\beta_N} f_N(k/N)
 ={}&N\int_{\alpha_N}^{\beta_N}
       \frac{f_N(x+iH)}{1-e^{2\pi iN(x+iH)}}\,dx\\
 &+N\int_{\alpha_N}^{\beta_N}
       f_N(x-iK)\frac{e^{-2\pi iN(x-iK)}}
                         {1-e^{-2\pi iN(x-iK)}}\,dx\\
 &-iN\int_{-K}^{H}
       \frac{f_N(\beta_N+iy)-f_N(\alpha_N+iy)}
                                      {1+e^{-2\pi Ny}}\,dy .
 \end{split}                                                     \tag{30}
\]
It follows by the same residue calculation as equation (5) of
[the full-period contour identity](research_mixed_pair_full_period_contour.md);
the two horizontal heights need not be equal.

For the upper parts of the vertical sides, there is no omitted
penalty. Their rates are convex in \(y\), and both endpoint
rates are below \(M\): the real endpoints by (20), (23), and
the top endpoints by strict horizontal concavity.
For the lower parts, subtract \(2\pi|y|\); convexity remains,
and both endpoint rates are below \(M\) by the real endpoint
bounds and (29). This controls every vertical term in (30).
The \(O(N^{-1})\) movement to the half-grid changes the compact
rates by \(O(N^{-1})\), so all strict gaps persist.
No Fourier correction or endpoint loop has been discarded.

The remaining principal horizontal integral has the sole
nondegenerate saddle \(z_*\) and strictly concave real action.
Substituting (14) and applying its Gaussian integral gives
\[
 \sum_{k=0}^{N-1}
       \frac{X^{D-k}Q^{k(k+1)}(X;Q)_k}{F_k^3}
  =N^{-1}B(X)e^{NS(X)}(1+O(N^{-1})),                            \tag{31}
\]
where, on a sufficiently small fixed complex disk about \(X_*\),
\[
 S(X)=\Phi(z(X);X),\qquad
 B(X)=b(z(X);X)\sqrt{\frac{2\pi}{-\Phi_{zz}(z(X);X)}} .
 \tag{32}
\]
The saddle, its Gaussian branch, and all factors are continued
from the contour just proved. In particular \(B\) is holomorphic
and nonzero. Strict gaps on compact contours persist on this disk;
one can move the principal horizontal segment slightly through
the continued saddle. All normalized errors are holomorphic.

**Theorem 3.** The actual original clock polynomial satisfies
\[
 \boxed{\quad
 G_N(X)=A_NB(X)e^{NS(X)}(1+O(N^{-1}))
       =N^{-1/2}\omega_NB(X)e^{NS(X)}(1+O(N^{-1}))
 \quad}                                                        \tag{33}
\]
uniformly on a fixed disk about \(X_*\), at both parities.
Every fixed derivative of the normalized error has the same
bound on smaller disks.
For the negative original crossing, conjugate the coefficients:
\(G_{N,-}(X)=\overline{G_N(\overline X)}\). The corresponding
disk is centered at \(\overline{X_*}\), and its phase and
amplitude are \(\overline{S(\overline X)}\) and
\(\overline{B(\overline X)}\), with the original scalar
\(\overline{\omega_N}\).

*Proof.* Multiply (31) by the exact factor \(A_NN\) in (5).
The whole error polynomial \(\mathcal G_{\delta_N}\) is
polynomially bounded there by Lemma 1. Since \(\operatorname{Re}
S>1/20\) after a further disk shrink and \(|A_N|\asymp
N^{-1/2}\), that error is exponentially smaller than the
displayed nonzero main term. Equation (2) gives the second form.
Uniform holomorphic estimates and Cauchy's formula give all
fixed derivatives. \(\square\)

## 5. The finite scalar enclosures

The only finite analytic inputs to the contour proof are (20)
and the unexponentiated equation
\(\Phi_z(z_*;X_*)=0\). They concern the single algebraic root
(15), the quadratic saddle (18), and two dilogarithmic values.
There is no high-dimensional contour covering.

For outward evaluation one may use
\[
 \begin{split}
 \mathcal J(z)
   &=\frac{i\pi}{2}(z-z^2)
       +\frac{i}{2\pi}
          \{\operatorname{Li}_2(e^{2\pi iz})-\pi^2/6\},\\
 \int_0^z\operatorname{Log}(1-Xe^{2\pi it})\,dt
   &=\frac{i}{2\pi}
       \{\operatorname{Li}_2(Xe^{2\pi iz})-\operatorname{Li}_2(X)\}.
 \end{split}                                                     \tag{34}
\]
At \(z_*\), all dilogarithm arguments have modulus below one.
At the real point \(\beta=3/10\), the one unit-modulus
argument is separated from its branch point and has the
ordinary continued value. The prescribed logarithms in (12)
fix the value of the gradient before exponentiation.

The approximate locations, solely to identify the finite
certificate targets, are
\[
 \begin{split}
 X_*&\approx-0.254366120317032-0.577475749602808i,\\
 z_*&\approx0.150261985320321+0.075692709209091i,\\
 \operatorname{Re}S(X_*)&\approx0.053613309263570,\\
 \operatorname{Re}\Phi(3/10;X_*)&\approx-0.011703587886202 .
 \end{split}                                                     \tag{35}
\]
These decimal values are not used as inequalities. The
[exact rational certificate](../experiments/verify_next_crossing_complex_phase.py)
and its
[saved result](../repro/results/research-next-crossing-complex-phase.json)
prove every strict bound in (20). They first isolate \(\tau\)
in a radius-\(10^{-14}\) disk by Rouché's theorem, contained
in the previously selected geometric root disk, and then form
\(X_*=1/(\tau^2-3\tau+3)\), \(Y_*=1/\tau\).

All asserted operations use rational intervals rounded outward
to denominator \(10^{50}\). The value of \(\pi\) uses Machin's
arctangent identity with 90 terms and its explicit alternating
tail. Right-half-plane logarithms use 250 terms of
\[
 \operatorname{Log}z=
 2\sum_{n\ge0}\frac{((z-1)/(z+1))^{2n+1}}{2n+1};
\]
the clock is rotated to \(iX_*\), and its argument is restored
by subtracting \(\pi/2\). Dilogarithms in the open unit disk
use 250 terms and the tail bound
\(r^{251}/(251^2(1-r))\). For the single unit-modulus
argument \(Y=e^{3\pi i/5}\) at the real cutoff, the identity
\[
 \operatorname{Li}_2(Y)=
 -\operatorname{Li}_2\!\left(\frac{Y}{Y-1}\right)
                         -\tfrac12\operatorname{Log}^2(1-Y)
\]
moves the dilogarithm into the open unit disk.
The principal branches follow by continuation along \(tY\),
\(0\le t\le1\), since \(\operatorname{Re}Y<0\).
The resulting intervals include
\[
 \begin{split}
 0.05361330926322
  &<\operatorname{Re}\Phi(z_*;X_*)<0.05361330926392,\\
 -0.01170358788634
  &<\operatorname{Re}\Phi(3/10;X_*)<-0.01170358788607.
 \end{split}
\]
The record retains the exact rational endpoints, root inclusion,
and script hash.

## 6. The retained clock sheet and remaining boundary operation

The full polynomial has a second exact expression:
\[
 \begin{split}
 H_N(Z)&=\sum_{\ell=0}^{D}
        \frac{(Z;Q)_\ell(-1)^\ell Q^{\ell(\ell+1)/2}}{F_\ell^2},\\
 G_N(X)&=X^D H_N(Q/X),\\
 \gamma_{D-r}&=N(-q^{-1})^r H_N(Q^{-r}).
 \end{split}                                                     \tag{36}
\]
The apparent negative powers cancel because \(H_N\) has degree
at most \(D\). To derive these expressions, the original braid
identity gives \(MJ\alpha=\kappa J M^{-1}(JM^2\mathbf e_0)\),
while the two-crossing terminal has coefficients
\(Nq^{\ell^2}/F_\ell\). Substitution of the original inverse
crossing matrix yields
\[
 \gamma_{D-r}
 =N(-q^{-1})^rF_r
   \sum_{\ell=0}^r
       \frac{Q^{\ell^2-r\ell}}{F_\ell^2F_{r-\ell}} .
\]
Now use
\((Q^{-r};Q)_\ell=(-1)^\ell
Q^{-r\ell+\ell(\ell-1)/2}F_r/F_{r-\ell}\).
This gives (36), with its finite sum terminating automatically
at \(\ell=r\). The equality for \(G_N\) follows from (4) at
all \(N\) clock roots and ordinary polynomial uniqueness.
The precise polynomial defect is
\[
 \begin{split}
 &(Z-Q)H_N(Z/Q)-(3Z-1-Q)H_N(Z)
                   -(Z-1)^2H_N(QZ)\\
 &\hspace{35mm}=-\frac{Z^2}{N^2}\frac{Z^N-1}{Z-Q}.
 \end{split}                                                     \tag{37}
\]
For example, the original recurrence gives its zeros at all
\(N\)-th roots except \(Q\). The left side has a double zero
at \(Z=0\), degree at most \(N+1\), and leading coefficient
\(-1/N^2\); these determine (37). The two coefficients at zero
cancel directly, for any polynomial substituted in place of
\(H_N\).

After reversal this becomes
\[
 \begin{split}
 &(1-X/Q)^2G_N(X/Q)
       +X[3-(1+Q^{-1})X]G_N(X)\\
 &\hspace{16mm}-QX(1-X)G_N(QX)
                =\frac{1-X^N}{N^2(1-X)},\qquad G_N(0)=N^{-2}.
 \end{split}                                                     \tag{38}
\]
The right side is an ordinary polynomial, including at \(X=1\).
In particular the actual interpolation does not satisfy a
homogeneous equation away from the physical grid.

For noninteger \(j=Nx\), principal logarithms obey
\[
 \operatorname{Log}(-q)=-i\pi+i\pi/N,\qquad
 \operatorname{Log}(-q^{-1})=i\pi-i\pi/N.
 \tag{39}
\]
Their ratio to the power \(Nx\) is \(X^{N-1}\), where
\(X=e^{-2\pi ix}\), not merely \(X^{-1}\). The latter equality
holds only at physical colors. The polynomial and all explicit
chirps in (4), (36) fix the sheet used by (33).

The remaining full ordinary boundary polynomial is still
\[
 F_N(w)=\mathbf e(w)^TJM^2\gamma,\qquad
 \mathbf e(w)=(e_0(w),\ldots,e_D(w))^T .
 \tag{40}
\]
Its exact row is supplied by the full degree-two power-two
kernel:
\[
 (\mathbf e(w)^TJM^2)_j
   =N\sum_{i+j<N}q^{(i-j)^2}
              \frac{F_{i+j}}{F_i^2F_j^2}\,e_i(w).
 \tag{41}
\]
All indices and ordinary \(w\)-derivatives remain in (41).
At odd \(N\), some value terms vanish at \(w=-2\), but their
normal derivatives cannot be removed.
The nonzero complex profile (33) is an input to the coherent
pairing (40); proving survival of its selected contribution in
that pairing is a further task.

The focused
[original polynomial checker](../experiments/check_three_crossing_complex_polynomial.py)
and its
[saved result](../repro/results/research-three-crossing-complex-polynomial.json)
compare (3)--(5), (36)--(38), and their ordinary derivatives with
independently formed original matrices at \(N=2,\ldots,15\),
for both signs. They also retain arbitrary input columns and
the noninteger chirp identity (39).
These finite diagnostics test exact normalization; the
asymptotic theorem follows from the complete contour proof
and the outward inequalities in Section 5.

## 7. Calibration against the original real-color phase

Write
\[
 X=e^{-2\pi ix},\qquad
 \tau(x)=\frac{3-\sqrt{4/X-3}}2,\qquad
 \lambda=\frac{3-2X+\sqrt{4/X-3}}2,\qquad
 \mu=\frac{3-2X-\sqrt{4/X-3}}2 .
 \tag{42}
\]
The square root starts at one when \(x=0\). Let
\[
 I(x)=\int_0^x\operatorname{Log}\lambda(t)\,dt,\qquad
 a(x)=\sqrt{\frac{\lambda(x)}{\lambda(x)-\mu(x)}},
 \qquad a(0)=1 .
 \tag{43}
\]
These are the phase and amplitude of
[the original local profile](research_three_crossing_next_crossing_dominant_profile.md).
The following identities use their specified continuation, not
an arbitrary logarithm of the algebraic critical equations.

Continue first along the real interval \(0<x\le x_0\), where
\(x_0=\operatorname{Re}[-\operatorname{Log}X_* /(2\pi i)]\),
and then vertically to
\(x_*=-\operatorname{Log}X_* /(2\pi i)\).
On the real leg, \(|\tau|=1\) would imply
\[
 |\tau^2-3\tau+3|^2=1+12(1-\operatorname{Re}\tau)^2.
 \tag{44}
\]
Since \(|X|=1\), this forces \(\tau=1\), excluded away from
\(x=0\). At \(x_0>3/10\), one has
\(\operatorname{Re}(4/X-3)<-4\), hence
\(|\operatorname{Im}\tau|>1\). By continuity the entire open
real leg therefore has \(|\tau|>1\).
On the vertical leg, \(\arg X\) is fixed and \(|X|\)
decreases, so the same real-part inequality persists.
Thus \(|\tau|>1\), \(|Y|<1\), and \(|XY|<1\) on the whole
path, where \(Y=1/\tau\). All the stationary dilogarithms and
logarithms used in (12) continue regularly along this path.
The argument is not an assertion about every point of the
lower half-strip.

The critical equation is zero on this continuation, with the
charge fixed in Section 3. Differentiating the stationary
action gives
\[
 \frac{d}{dx}S(X(x))
   =\operatorname{Log}Y+\operatorname{Log}(1-X)
       -\operatorname{Log}(1-XY)-2\pi i .
 \tag{45}
\]
The algebraic identities
\[
 \begin{gathered}
 r=\tau^2-3\tau+3,\qquad
 \lambda=-\frac{(\tau-2)^3}{r},\qquad
 \mu=\frac{(\tau-1)^3}{r},\\
 \frac{Y(1-X)}{1-XY}
   =\frac{\tau-2}{(\tau-1)^2}
   =\frac{\lambda}{4\sin^2\pi x}
 \end{gathered}                                                   \tag{46}
\]
show equality of the exponentiated logarithms. As \(x\to0+\),
the imaginary parts of both retained logarithms of this last
ratio tend to zero. Their integer difference is therefore zero,
and remains zero on the specified path.
The stationary action tends to zero as \(x\to0+\):
this follows directly from (12), or the continuous endpoint
values of the dilogarithms in (34).
Since \(I(x)\) and \(\mathcal J(x)\) also tend to zero, (45)
integrates to the exact action calibration
\[
 \boxed{\qquad
 S(X(x))=I(x)-2\mathcal J(x)-2\pi ix
                  =I(x)-2\mathcal J(x)+\operatorname{Log}X .
 \qquad}                                                        \tag{47}
\]
It holds on the local geometric disk by holomorphic continuation.

There is also an algebraic amplitude comparison. Put
\[
 \mathcal D=2+\frac{3Y}{1-Y}-\frac{XY}{1-XY},
 \qquad \Phi_{zz}=2\pi i\mathcal D .
 \]
Squaring the exact Gaussian amplitude (32) gives
\[
 B(X)^2
   =-\frac{Y^2(1-X)}
       {X^2(1-Y)^3(1-XY)\mathcal D}
   =\frac{\lambda}
       {X^2\,4\sin^2(\pi x)(\lambda-\mu)}
   =\left(\frac{a(x)}{2X\sin\pi x}\right)^2 .
 \tag{48}
\]
The middle equality is a rational identity after substituting
\(X=1/r\), \(Y=1/\tau\). It does not remove the Gaussian
branch fixed by the actual contour.
The rational certificate in Section 5 also checks this identity
symbolically and evaluates both proposed amplitudes with their
specified principal logarithms. The continuation of \(a\) is
its principal square root: along the chosen path both
\(3-2X\) and \(\sqrt{4/X-3}\) lie in the first quadrant, so
\(\operatorname{Re}[\lambda/(\lambda-\mu)]>1/2\).
Both imaginary parts are greater
than \(4/5\) at \(X_*\). Hence they are the same square root,
not its negative. Holomorphic continuation gives
\[
                 \boxed{\quad B(X)=\frac{a(x)}{2X\sin\pi x}.
                        \quad}                                 \tag{49}
\]

**Corollary 4.** The canonical analytic extension of the original
next-crossing column,
\[
 \gamma_N^{\mathrm{can}}(x)=
 N\kappa^2 e^{Nx\operatorname{Log}(-q^{-1})}
                              G_N(e^{-2\pi ix}),
 \tag{50}
\]
agrees with \(\gamma_j\) at every physical color \(x=j/N\).
On a fixed complex disk about \(x_*\), it has the nonzero
profile
\[
 \gamma_N^{\mathrm{can}}(x)=
 \gamma_0 e^{Nx\operatorname{Log}(-q)}
 \frac{a(x)e^{NI(x)}}{\mathfrak G_N(Nx)^2}
                                      (1+O(N^{-1})).
 \tag{51}
\]
The errors are uniform and holomorphic; their fixed derivatives
have the same bound on smaller disks.

*Proof.* Equations (33), (47), and (49) give the result after
retaining the exact principal-chirp identity (39). For the
initial scalar, the full endpoint formula gives the exact
relation
\[
                  \gamma_0=N^2\kappa^2 A_D.
 \]
The reflected factorial tail gives \(A_N-A_D=O(N^{-2})\),
whereas \(|A_D|\asymp N^{-1/2}\). Thus replacing \(A_N\)
by \(A_D\) costs a relative \(O(N^{-3/2})\).
The canonical sine-factorial expansion supplies
\(\mathfrak G_N(Nx)^2=
2N\sin(\pi x)e^{2N\mathcal J(x)}(1+O(N^{-1}))\).
Finally the ratio of the principal chirps is \(X^{N-1}\),
as in (39), exactly the power required by the action and
amplitude calibrations. This proves (51) with the original
\(\gamma_0\), including both parities. \(\square\)

This complex extension is proved from the finite sum and its
whole contour. It is not inferred solely by analytically
continuing an \(O(N^{-1})\) asymptotic known on real colors.
