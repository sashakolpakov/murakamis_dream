# Actual fixed-width Gauss coherent boundaries from the complete input sum

Private written proof, 18 November 2026.

The original ordinary-binomial input of the actual Gauss first row can
be summed before taking any asymptotic limit. At every fixed width this
gives two scalar coefficient integrals. Their original circles select a
nonzero branch on a specified small input sector. The competing vacuum
in the wider boundary is retained and estimated on the entire circle.

This is an actual coherent boundary theorem. It does not apply a
binomial transform to an error estimate for a monomial kernel, and it
does not yet propagate the coherent boundary to nonzero output
activities. The smaller sector below is essential for the proof.

## 1. Literal matrix row and its two coefficient integrals

Use the notation and actual matrices of the complete direct W:
\[
 c_0=2\pi i,\quad q=e^{\pi i/N},\quad Q=q^2,\quad d=N-1,\quad
 x=-q^{-1},\quad f_a=(Q;Q)_a.
 \tag{1}
\]
Fix a number \(r\ge2\) of tail heads, put \(s=r-1,\ p=r-2\), and
restrict to integer degree \(T\le d\), where
\[
 \sigma_N=(T+1)/N\in I\Subset(1/2,1),\qquad
 \tau=T/N,\quad C=Q^{-T-1},\quad K_{r,T}=x^rQ^{-T}.
 \tag{2}
\]
The original simplex basis is
\[
 |\beta\rangle=|\beta_1,\ldots,\beta_s,T-|\beta|\rangle,
 \qquad \beta_i\ge0,\quad |\beta|\le T.
\]
Write \(A=A_N^{(r)}\) for W's actual operator and retain its vacuum
entry exactly:
\[
 a_{00}^{(r)}=(-1)^d N K_{r,T}^d v_r,\qquad
 v_r=V_0^{(r)},\qquad
 V_a^{(r)}=\sum_{n=a}^T Q^{n(n+r-1)}
                 {T\brack n}_Q{T-a\brack n-a}_Q.
 \tag{3}
\]
W proves \(v_r\ne0\) for all sufficiently large \(N\), uniformly in
(2). Set \(G_r(t)=\sum_{a=0}^T(V_a^{(r)}/v_r)t^a\).

The matrix \(A\) is symmetric in this original bilinear basis.
Indeed the literal root head actions give
\(E^t=x^{-1}KF,\ F^t=xEK^{-1}\); the ordered coproduct gives the
same identities for a total on any interval. The Cartan factors
cancel in \((F^nE^n)^t\), so each term of W's ordered formula
\[
 A=(-1)^dN\sum_{n=0}^d(-1)^nq^{n^2}F^nE^nK^{d-n}/f_n^2
\]
is symmetric on fixed degree. W's first-column formula consequently
gives the exact first row
\[
 \frac{A_{\mathbf0,\beta}}{a_{00}^{(r)}}
       =\frac{V_{|\beta|}^{(r)}}{v_r}
                         \prod_{i=1}^s c_i^{\beta_i},
 \qquad c_i=x^{r-i}.
 \tag{4}
\]
Symmetry here is only a finite matrix identity; it is not a positive
pairing or a replacement of the right coherent dual.

Retain that dual literally. On \(z_r\ne0\), put
\[
 \xi_i=c_i z_i/z_r,\qquad
 c_T(z)=\sum_{|\beta|\le T}
    \binom d{T-|\beta|}\prod_{i=1}^s\binom d{\beta_i}
       z_r^{T-|\beta|}\prod_{i=1}^s z_i^{\beta_i}|\beta\rangle.
 \tag{5}
\]
Define the normalized coherent boundary
\[
 \mathcal C_{r,N,T}(\xi)=
       \frac{\langle\mathbf0|A c_T(z)\rangle}
                {a_{00}^{(r)}z_r^T\binom dT}.
 \tag{6}
\]
Every factorial dual and every physical cap in (5) is present.

The finite ordinary-binomial polynomial
\[
 \mathcal B_{r,N,T}(z)=
   \binom dT^{-1}[u^T](1+u)^d\prod_{i=1}^s(1+u z_i)^d
 \tag{7}
\]
gives the exact identity
\[
 \boxed{\quad
 \mathcal C_{r,N,T}(\xi)=
      \operatorname{CT}_t\,G_r(t)
                   \mathcal B_{r,N,T}(\xi_1/t,\ldots,\xi_s/t).
 \quad} \tag{8}
\]
To check it, the coefficient of \(z^\beta\) in (7) is
\(\binom dT^{-1}\binom d{T-|\beta|}\prod_i\binom d{\beta_i}\).
The \(t\)-constant term pairs this coefficient only with
\(V_{|\beta|}^{(r)}/v_r\). This proves (8) for the entire finite
sum. In particular all inactive magnetic indices have already been
summed; no small-slope approximation is used to obtain (8).

## 2. The complete multivariate binomial coefficient circle

There is a fixed small polydisk \(|z_i|<\epsilon\), uniform in (2),
on which (7) has the actual asymptotic
\[
 \mathcal B_{r,N,T}(z)=e^{N S_B(z;\tau)}
                 A_B(z;\tau)(1+O(N^{-1})).
 \tag{9}
\]
The error is holomorphic, with fixed derivatives on smaller
polydisks. All functions in this assertion keep \(\tau=T/N\)
exactly, not \(\sigma_N\).

Here are the phase, amplitude and complete-circle proof. Let \(u=u(z)\)
be the analytic solution near \(b=\tau/(1-\tau)\) of
\[
 \frac{u}{1+u}+\sum_{i=1}^s\frac{uz_i}{1+uz_i}=\tau.
 \tag{10}
\]
The derivative in \(\log u\) at \(z=0\) is
\(\tau(1-\tau)>0\), uniformly. Put
\[
 \begin{split}
 S_B(z;\tau)&=\log(1+u)+\sum_i\log(1+uz_i)-\tau\log u\\
       &\hspace{12mm}+\tau\log\tau+(1-\tau)\log(1-\tau),\\
 D_B(z;\tau)&=\frac{u}{(1+u)^2}
                         +\sum_i\frac{uz_i}{(1+uz_i)^2},\\
 A_B(z;\tau)&=
   \frac{\sqrt{\tau/(1-\tau)}}
                {(1+u)\prod_i(1+uz_i)\sqrt{D_B(z;\tau)}}.
 \end{split} \tag{11}
\]
All logarithms and the Gaussian square root are continued from \(z=0\).
Thus \(S_B(0)=0,\ A_B(0)=1\), and
\[
                    \partial_{z_i}S_B(0)=b.
 \tag{12}
\]

Use the actual coefficient circle \(u=u(z)e^{i\theta}\) in (7).
It is a positive circle about zero; changing its complex radius is
allowed because the coefficient integrand has no other poles. At
\(z=0\), the real phase loss is
\[
 \log\frac{|1+b e^{i\theta}|}{1+b}
    =\tfrac12\log\left(1-
       \frac{4b}{(1+b)^2}\sin^2(\theta/2)\right)
                 \le -c(1-\cos\theta).
 \tag{13}
\]
The compact range of \(\tau>1/2\) keeps \(b\) bounded above and a
positive distance from \(1\), so the logarithm can be differentiated
on this circle without a zero. Its possible winding changes only the
imaginary lift; the original coefficient integrand is single-valued.
For small complex \(z\), the saddle condition (10) makes the first
\(\theta\)-derivative vanish at zero. The difference from the phase
at \(z=0\) has uniformly small second derivative on the circle.
Near zero this preserves the quadratic bound in (13); away from
zero its uniform smallness preserves the fixed gap. Thus the whole
circle, including its complement, has a unique real maximum at the
chosen saddle after the polydisk is shrunk.

The coefficient integrand, written with \(N\) in the exponent, has
amplitude \([(1+u)\prod_i(1+uz_i)]^{-1}\). Taylor expansion on the
central arc with the bound (13) therefore gives
\[
 [u^T](1+u)^d\prod_i(1+uz_i)^d
 =\frac{e^{N[S_B-\tau\log\tau-(1-\tau)\log(1-\tau)]}}
        {\sqrt{2\pi N D_B}\,(1+u)\prod_i(1+uz_i)}
       (1+O(N^{-1})).
 \tag{14}
\]
The coefficient of this Gaussian is one: it is the original positively
oriented circle and the square root is positive at \(z=0\).
Finally
\[
 \binom{N-1}T=
 \frac{\sqrt{(1-\tau)/\tau}}{\sqrt{2\pi N}}\,
 e^{-N[\tau\log\tau+(1-\tau)\log(1-\tau)]}
       (1+O(N^{-1})).
 \tag{15}
\]
Division proves (9)--(11), including every \(d=N-1\) amplitude
factor. The uniform holomorphic error and its derivatives follow by
working on a slightly larger polydisk first. In particular (9)
also gives the absolute bound
\[
                |\mathcal B_{r,N,T}(z)|\le C e^{N\Re S_B(z;\tau)}
 \tag{16}
\]
throughout a smaller whole polydisk.

## 3. The outer saddle and the honest input sector

For clarity distinguish the constants
\[
        a=2/c_0,\qquad b=\tau/(1-\tau),\qquad
        b_C=C^{-1}-1.
 \tag{17}
\]
The scalar boundary data supplied by W are \(\phi(t;C), A_G(t;C)\)
and \(Y_B(t;C)\), with \(\phi(0)=0,\ \phi'(0)=a\). Define
\[
 W(t;C)=\frac{C^{-1}-Y_B(t;C)}t,\qquad
 A_r^\partial(t;C)=
                 \frac{p!\,A_G(t;C)W(t;C)^p}{(a b_C)^p}.
 \tag{18}
\]
On a sufficiently small punctured disk \(W\) has no zeros.
W proves both the whole-disk competing bound
\[
 |G_r(t)|\le C_r(1+e^{N\Re\phi(t;C)})
 \tag{19}
\]
and, on compact sets with \(\Re\phi(t;C)>0\),
\[
 G_r(t)=N^{-p}e^{N\phi(t;C)}
                          A_r^\partial(t;C)(1+O(N^{-1})).
 \tag{20}
\]
The vacuum summand in (19) cannot be removed on the entire circle.

Choose a bounded open domain of complex shapes
\(\vartheta=(\vartheta_1,\ldots,\vartheta_s)\) with
\(\sum_i\vartheta_i=1\), with openness relative to that affine
hyperplane. Work uniformly on its compact subsets; zero coordinates
are allowed. Use the
input coordinates
\[
        \xi_i=\frac{\vartheta_i a_*^2}{a b},\qquad
        0<|a_*|<a_0,\qquad
        |\arg a_*|<\theta_0<\pi/3.
 \tag{21}
\]
The shapes and the square-root choice describe a genuine open input
sector when \(\sum_i\xi_i\ne0\). Estimates below are uniform on compact
subsets of this punctured sector and the shape domain. They do not
assert a uniform limit when \(N|a_*|\) stays bounded.

Let
\[
 F(t)=\phi(t;C)+S_B(\xi_1/t,\ldots,\xi_s/t;\tau).
 \tag{22}
\]
After setting \(t=(a_*/a)v\), its leading expression is
\(a_*(v+v^{-1})+O(a_*^2)\). The equation \(D_tF=0\) consequently
has a unique analytic solution near \(v=1\):
\[
 \begin{split}
 t_*&=(a_*/a)(1+O(a_*)),\\
 \Psi(\xi;C,\tau)&=F(t_*)=2a_*+O(a_*^2),\\
 \mathcal H&=D_t^2F(t_*)=2a_*+O(a_*^2).
 \end{split} \tag{23}
\]
Here and below \(D_t=t\partial_t\). The implicit derivative after
dividing the saddle equation by \(a_*\) is \(2\) at \(v=1\).
Thus these are actual analytic functions, not just formal expansions.
Their estimates are uniform for the stated compact shape set.

Use the original constant-term circle \(t=t_*e^{i\theta}\).
Both \(t\) and all \(\xi_i/t\) remain inside the disks of (9),(19).
On this circle the combined phase satisfies
\[
 \Re[F(t_*e^{i\theta})-F(t_*)]
 \le-[2\Re a_*-C|a_*|^2](1-\cos\theta).
 \tag{24}
\]
Indeed its leading expression is \(2a_*\cos\theta\). The periodic
analytic remainder has second derivative \(O(|a_*|^2)\), and its
first derivative at zero is zero because \(t_*\) is the exact
saddle. Integration of that derivative bound on \([-\pi,\pi]\)
gives (24).

There is a separate estimate for the vacuum part of (19):
\[
 \max_\theta\Re S_B(\xi/t_*e^{-i\theta};\tau)
                       \le |a_*|+C|a_*|^2.
 \tag{25}
\]
By contrast \(\Re\Psi=2\Re a_*+O(|a_*|^2)\). Therefore (21)
and a sufficiently small \(a_0\) give
\[
 \Re\Psi-\max_\theta\Re S_B(\xi/t_*e^{-i\theta};\tau)
          \ge \tfrac12(2\cos\theta_0-1)|a_*|>0.
 \tag{26}
\]
This is why the sector is restricted to \(\theta_0<\pi/3\).
The envelope allowed by (19),(16) has leading maximum
\(\max(|a_*|,2\Re a_*)\); a sector approaching \(\pi/2\) would
not establish (26).

Choose a fixed small central arc about \(\theta=0\). On that arc
\(\Re\phi(t_*e^{i\theta};C)>0\), uniformly on every compact
subset of (21), so (20) applies with holomorphic relative error.
On the complementary arc, (19),(16),(24),(26) bound the whole
integrand by the sum of two exponentials with a strict gap below
\(\Re\Psi\). Relative to the central amplitude this remains
exponentially small despite the factor \(N^p\). This estimates every
competing boundary branch and all finite caps through the actual
polynomials in (8).

## 4. Actual coherent boundary and its normalization

On the central arc substitute (9),(20) into (8). Taylor expansion
at the exact saddle, followed by (24)--(26), gives
\[
 \boxed{\quad
 \mathcal C_{r,N,T}(\xi)=
   N^{-p}\frac{e^{N\Psi(\xi;C,\tau)}}{\sqrt{2\pi N\mathcal H}}\,
      A_r^\partial(t_*;C)
      A_B(\xi_1/t_*,\ldots,\xi_s/t_*;\tau)
               (1+O(N^{-1})).
 \quad} \tag{27}
\]
The Gaussian square root is continued from positive real \(a_*\);
\(\mathcal H=2a_*+O(a_*^2)\) has positive real part on a sufficiently
small sector. Its coefficient is one, because the positive circle
in (8) passes once through the selected saddle and the full
complement was just bounded. All displayed amplitude factors are
nonzero. Fixed input and shape derivatives follow on smaller compact
sets by Cauchy; the sector coordinate is locally invertible for
\(a_*\ne0\).

In particular the original, unnormalized boundary is
\[
 \boxed{\begin{split}
 \langle\mathbf0|A_N^{(r)}c_T(z)\rangle
   ={}&a_{00}^{(r)}z_r^T\binom dT\,
      N^{-p}\frac{e^{N\Psi}}{\sqrt{2\pi N\mathcal H}}\,
      A_r^\partial(t_*;C)A_B(\xi/t_*;\tau)\\
      &\hspace{32mm}\cdot(1+O(N^{-1})).
 \end{split}} \tag{28}
\]
Neither the width-dependent vacuum normalization nor the physical
phases \(c_i=x^{r-i}\), nor the homogeneous character \(z_r^T\),
nor the binomial factor has been omitted. The normalized action is
calibrated by \(\Psi\to0\) as \(a_*\to0\), while (27) is only a
punctured-sector asymptotic. The exact expression (8) remains valid
in the microscopic region where this Gaussian approximation is not
uniform.

The selected input sector is all-width and allows bounded complex
shapes without requiring each \(\xi_i\) to have a nonzero phase slope.
Its proof used the full original input sum, not a termwise transform
of the monomial approximation. This distinction is material:
inactive Cauchy interfaces can create an extensive phase even when
the corresponding monomial phase is constant.

The output in (28) is still the literal vacuum row. A theorem for
nonzero output activities would need propagation of this coherent
initializer with the exact binomial-conjugated input operators and
their retained endpoints. No such propagation is asserted here.
Nor does (28) estimate the exterior braid, turnover, inverse Cartan
factor or closed source in the original opposite kernel. The proof
is at fixed \(q_N,M=1\) and physical integer \(T\); it gives no
meridian normal, complex-degree interpolation or geometric-cycle
coefficient.

## 5. Complete direct and protocol

The sole complete proof direct is:

* **W:** [research_fixed_width_gauss_boundary_branches.md](research_fixed_width_gauss_boundary_branches.md),
  427 lines, SHA256
  cdcb82d2bd48948ff45baaec65a71f639607e10a9bc12acff344e34ae972d404.

W supplies the actual first column and vacuum normalization, the
marked phase/amplitude, and the whole-disk competing bound. The
matrix transpose, exact ordinary-binomial contraction, its inner
coefficient saddle and the complete outer-circle selection are
proved here. Only written mathematics and text/hash operations are
used; frozen and public files are unchanged.

Author freeze protocol: the entire matching final was freshly reread
nontruncated. The sole complete direct W was freshly read in full in
this author sequence and retained unchanged. Every used implication
was checked, and both hashes were renewed. Independent matching
review and parent adoption remain separate.
