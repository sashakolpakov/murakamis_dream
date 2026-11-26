# The rescaled full-clock germ has an explicit exceptional character

Private written proof, 18 November 2026.

The convergent initial family in [D] has an explicit restriction after
the simultaneous scaling \(m=\nu/(Y-\alpha)\). The calculation uses the
marked determinant of the same highest-cut source. No averaging of the
cut, inverse of its projector, or analytic continuation of an inserted
minor is used.

## 1. Marked determinant and its simple pole

Use [M]'s fixed path-index coordinates \(k\in\mathbb Z^s\). Let \(t\)
mark them by \(e^{t\cdot k}\), independently of \(h=\log Q\), and write
\[
 \mathscr F(h,Y,t)
   =\mathcal W_\beta(1-e^h,Y;e^t)
   =\sum_{n\ge0}h^nF_n(Y,t).
 \tag{1}
\]
This is the original highest-cut source, with its pivots and framing.
On a local square-root chart \(x_0^2=Y\), put
\[
 B(Y,t)=L_\beta(x_0,e^t)T_0,\quad
 K(Y,t)=I-B(Y,t),\quad
 D(Y,t)=\det K(Y,t),\quad
 T_0=\operatorname{diag}(0,1,\ldots,1).
 \tag{2}
\]
The whole marked determinant theorem in [M] implies
\[
                 F_n(Y,t)=\frac{P_n(Y,t)}{D(Y,t)^{2n+1}},
 \tag{3}
\]
where \(P_n\) is holomorphic near the point considered below. This
also holds in the coordinate \(h,Y\) of (1): converting \(1-Q\) to
\(h\) and \(x^2=Ye^{-h}\) uses an old order \(a\le n\) and at most
\(n-a\) meridian derivatives. Its denominator power is at most
\(2a+1+n-a\le2n+1\). Thus no marked quantum coefficient has been
omitted from (3).

Assume the simple Alexander root and actual simple two-branch node
of [D, (16)]. Write \(z=Y-\alpha\), and use its constants
\[
 r=\Delta_K'(\alpha)^{-1},\qquad
 \sigma=\frac{A}{2B_{\rm node}}\ne0,\qquad
 \eta_*=\frac1{4\sigma}.
 \tag{4}
\]
Here \(B_{\rm node}\) denotes [D]'s scalar node constant \(B\),
to distinguish it from the matrix in (2). Expanding [D, (22)] gives
\[
 c_n:=\left.z^{2n+1}F_n(\alpha+z,0)\right|_{z=0}
          =r\,\frac{(2n)!}{n!}\sigma^n.
 \tag{5}
\]

Since \(D(Y,0)=x_0^c\Delta_K(Y)\), its zero at \(Y=\alpha\) is
simple. The implicit-function theorem gives its unique local pole
curve \(Y=\alpha(t)\). Define
\[
 \mu_i=\partial_{t_i}\alpha(0)
       =-\frac{D_{t_i}(\alpha,0)}{D_Y(\alpha,0)}.
 \tag{6}
\]
These are derivatives of the actual marked source divisor.

They also have the stated corank-one formula with the cut retained.
Choose nonzero right and left null vectors \(u,v\) of \(K(\alpha,0)\).
A simple determinant zero forces corank one: otherwise its adjugate
would vanish and \(D_Y\) would be zero. Put
\[
 \kappa=v^TK_Yu,\qquad
 H_i=(\partial_{t_i}L_\beta)L_\beta^{-1}
                \quad\text{at }(\alpha,0).
 \tag{7}
\]
The local crossing substitutions and diagonal marks are invertible,
so the inverse of \(L_\beta\) is legitimate. The projector \(T_0\)
is never inverted. Writing \(\operatorname{adj}K=c_*uv^T\) gives
\(D_Y=c_*\kappa\ne0\). Since \(Bu=u\) and
\(\partial_{t_i}B=H_iB\), equation (6) becomes
\[
                         \mu_i=\frac{v^TH_i u}{\kappa}.
 \tag{8}
\]
No normalization \(v^Tu=1\) or algebraic simplicity of the eigenvalue
one is assumed.

## 2. Every highest inserted pole

For a fixed direction \(\nu\in\mathbb C^s\), set
\(y=\mu\cdot\nu\). The original degree-\(d\) index insertion is
\((\nu\cdot\partial_t)^dF_n(Y,t)|_{t=0}\). Equation (3) gives exactly
\[
 \left.
 z^{2n+d+1}
       (\nu\cdot\partial_t)^dF_n(\alpha+z,t)
 \right|_{t=0,z=0}
       =\frac{(2n+d)!}{(2n)!}\,y^d c_n.
 \tag{9}
\]
To verify this, locally write
\(D(Y,t)=d_0(Y,t)(Y-\alpha(t))\), with \(d_0\) a unit.
The pole of \(F_n\) is at most \(2n+1\). Achieving order
\(2n+d+1\) requires every derivative to differentiate that pole
once through the first derivative of \(\alpha\). The rising factorial
is \((2n+1)\cdots(2n+d)\). Any derivative on the holomorphic numerator
or unit, or any higher derivative of \(\alpha\), gives a smaller pole.
This proves (9), including \(d=0\), with its positive sign.
In particular quantum-coefficient derivatives are included and cannot
alter this highest pole.

## 3. Summing the actual convergent rescaled family

Let \(\mathcal B_m^{\rm pole}(z,\eta)\) be [D]'s initial full-clock
Borel germ. That theorem proves that
\[
 \mathcal G(z,\eta,\nu)
       =\mathcal B_{\nu/z}^{\rm pole}(z,\eta)
 \tag{10}
\]
extends holomorphically through \(z=0\), is entire in \(\nu\), and
converges on a common \(\eta\)-disk independent of \(\nu\).
This is an actual canonical germ, not a resummation chosen from its
highest coefficients.

At normal order \(h^{n+d}\), the degree-\(d\) clock term is
\((\nu\cdot k)^d/(d!z^d)\) inserted into order \(n\).
Equations (5) and (9), together with the Borel factor \(1/(n+d)!\),
therefore give
\[
 \mathcal G(0,\eta,\nu)
 =r\sum_{n,d\ge0}
       \frac{(2n+d)!}{n!\,d!\,(n+d)!}
             \sigma^n y^d\eta^{n+d}.
 \tag{11}
\]
Coefficient extraction is justified by the jointly convergent
extension (10); at each total \(\eta\)-degree the sum is finite.

Here is an elementary summation of (11). Put
\[
 C(t)=\frac{1-\sqrt{1-4t}}{2t},\qquad C(0)=1.
 \tag{12}
\]
For \(d\ge0\), define
\(J_d(t)=\sum_{n\ge0}\binom{2n+d}{n}t^n\).
For a fixed small circle \(|x|=\varepsilon\) and sufficiently small
\(|t|\), a convergent geometric series gives
\[
 J_d(t)=\frac1{2\pi i}\int_{|x|=\varepsilon}
              \frac{(1+x)^d}{x-t(1+x)^2}\,dx.
 \tag{12a}
\]
Its unique enclosed pole is \(x=C(t)-1\). The other root of the
quadratic denominator is outside the circle. At the enclosed root
the numerator is \(C(t)^d\) and the derivative of the denominator is
\(1-2tC(t)=\sqrt{1-4t}\). The residue theorem proves
\[
                         J_d(t)=\frac{C(t)^d}{\sqrt{1-4t}}.
 \tag{13}
\]
Apply (13) at \(t=\sigma\eta\) and sum the remaining exponential
series in \(d\). The exact answer is
\[
 \boxed{\displaystyle
 \mathcal G(0,\eta,\nu)
   =\frac{r}{\sqrt{1-4\sigma\eta}}\,
      \exp\!\left[
        \frac{\mu\cdot\nu}{2\sigma}
                  \bigl(1-\sqrt{1-4\sigma\eta}\bigr)\right].}
 \tag{14}
\]
The square root has value one at \(\eta=0\). Formula (14) agrees
with the canonical germ on its convergence disk and gives its
explicit two-sheet continuation as a function of \(\eta\) on the
exceptional divisor \(z=0\).

## 4. The exceptional odd coefficient

Write \(s=\sqrt{1-4\sigma\eta}\) and
\(a=(\mu\cdot\nu)/(2\sigma)\). Equation (14) is \(r e^a e^{-as}/s\).
Its odd and even parts under \(s\mapsto-s\) are respectively
\[
      r e^a\frac{\cosh(as)}s,\qquad
             -r e^a\frac{\sinh(as)}s.
 \tag{15}
\]
The second is holomorphic in \(s^2\). The coefficient of the odd
simple square-root pole is
\[
       \mathcal A(\nu)=r
                  \exp\!\left(\frac{\mu\cdot\nu}{2\sigma}\right).
 \tag{16}
\]
It is nonzero for every \(\nu\), and
\[
 \frac{\mathcal A(\nu+\nu')}{r}
       =\frac{\mathcal A(\nu)}r\frac{\mathcal A(\nu')}r.
 \tag{17}
\]
Thus the normalized coefficient is an exponential character of the
additive rescaled clock parameters. This statement uses the same
highest-cut source and its whole clocks.

It is only an exceptional initial character. It is not yet a character
of the full weight-zero classical Ward quotient at a nonzero meridian.
No continuation of the marked family through a characteristic
cofactor, marked finite-cutoff connection, or physical/geometric
identification follows from (14)--(17). The result applies to the
simple two-branch node in (4); no higher-collision profile is asserted.

The complete proof sources, read in full with their used implications
checked, are:

| Label | Complete direct source | SHA256 |
|---|---|---|
| D | notes/research_full_clock_initial_borel_family.md | d498ddfad641c85bba0257d22dcad53679ccd2cfb7e0c16f6cc790444f9e9b77 |
| M | notes/research_marked_verma_full_certificate_transport.md | a2d94711bb80e69139e25b4932f0878440934c0586ddd0535dc24fcfd61987b4 |

Only written mathematics, source reads and hash checks were used.
Frozen proofs and public documents are unchanged.
