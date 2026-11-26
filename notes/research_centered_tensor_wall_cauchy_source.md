# Exact wall values and a Cauchy representation of the centered source

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

Fixing one generating leg at any physical norm-wall point gives an
explicit product for the entire original three-boundary source.
This product is nonzero at every level when the other two arguments
lie in the open unit disk. Partial fractions then give a canonical
finite Cauchy representation of the full source, without a derivative
of a hypergeometric sum.

In the bulk of that wall, the product has a uniform asymptotic with
the initialized dilogarithmic action and a known nonzero amplitude.
The other two arguments may range over arbitrary compact complex
subsets of the disk. This is additional actual source control;
transport from this wall representation through the whole interior
still requires a separate estimate.

## 1. The original tensor and its forced connection

Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad \kappa=q^{d^2/2},\qquad
 D_N(t)=1-\eta t^N .
 \tag{1}
\]
Powers of \(q\) mean the displayed exponential, including fractional
powers. Put \(\mathbb D=\{t\in\mathbb C:|t|<1\}\).
Write \(\mathcal C_N(x,y,z)=\sum_{a,b,c=0}^{d}C_{abc}x^ay^bz^c\)
for the initialized centered tensor. It is the original full source
\[
 \mathcal C_N(x,y,z)=
 N^{-3/2}\phi\!\left(
             R^3G_N(x;\cdot)G_N(y;\cdot)G_N(z;\cdot)\right).
 \tag{2}
\]
Here \(R\) is the original positive crossing and \(\phi\) the
original Frobenius closing on
\(\mathcal H_N=\mathbb C[w]/(2T_N(w/2)+2)\), where
\(T_N(\cos\theta)=\cos(N\theta)\).
Every first derivative at a double Casimir root remains present.
The dot in (2) is the Casimir argument, not another generating leg.

The forced Rogers theorem proves the polynomial identity
\[
 \begin{split}
 &(1-Qxy)(1-Qxz)\mathcal C_N(Qx,y,z)
          -(1+qx)(1+qxyz)\mathcal C_N(x,y,z)\\
 &\hspace{22mm}
   =\beta_ND_N(y)D_N(z)\frac{xD_N(x)}{1+qx},
 \qquad
 \beta_N=\frac{(-1)^{N+1}\kappa^3}{N^{3/2}} .
 \end{split}
 \tag{3}
\]
The quotient on its right is a polynomial. The exact phase identities
\[
                \kappa^2=(-1)^Nq,\qquad
                \beta_N=-\frac{q\kappa}{N^{3/2}}
 \tag{4}
\]
will simplify the wall initializer. They follow directly from
\((N-1)^2=N^2-2N+1\).

For \(a\in\mathbb C\) and an integer \(j\ge0\), use
\[
                    (a;Q)_j=\prod_{h=0}^{j-1}(1-aQ^h).
 \tag{5}
\]
Empty products equal one. Define the wall points
\[
               X_j=-qQ^j,\qquad 0\le j<N .
 \tag{6}
\]
They are precisely the distinct zeros of \(D_N(x)\).

## 2. Every wall slice is an explicit nonzero product

**Theorem 1.** For every \(0\le j<N\) and \(y,z\in\mathbb D\),
\[
 \boxed{\quad
 \mathcal C_N(X_j,y,z)=
 \frac{\kappa}{\sqrt N}D_N(y)D_N(z)
       \frac{(Q;Q)_j(Qyz;Q)_j}
            {(-qy;Q)_{j+1}(-qz;Q)_{j+1}} .
 \quad}
 \tag{7}
\]
In particular each of these wall slices is nonzero on the whole
\(\mathbb D^2\), at every level and for both parities.

**Proof.** Evaluate (3) at \(x=-q^{-1}=X_d\). Its second
term vanishes. Since
\[
 \frac{D_N(x)}{1+qx}
                   =\sum_{h=0}^{N-1}(-qx)^h,
 \qquad
 \left.\frac{D_N(x)}{1+qx}\right|_{x=-q^{-1}}=N,
 \tag{8}
\]
equations (3)--(4) give the exact initial slice
\[
        \mathcal C_N(-q,y,z)=
       \frac{\kappa}{\sqrt N}
          \frac{D_N(y)D_N(z)}{(1+qy)(1+qz)} .
 \tag{9}
\]
For \(0\le j<N-1\), the forcing in (3) is zero at \(X_j\);
its displayed denominator is nonzero there. The remaining equation is
\[
 \frac{\mathcal C_N(X_{j+1},y,z)}
      {\mathcal C_N(X_j,y,z)}
  =\frac{(1-Q^{j+1})(1-Q^{j+1}yz)}
         {(1+qQ^{j+1}y)(1+qQ^{j+1}z)} .
 \tag{10}
\]
Starting with (9) proves (7). All divisions in this argument are
valid inside \(\mathbb D^2\): the linear factors involving
\(y,z\), and those involving \(yz\), cannot vanish there.
Also \((Q;Q)_j\ne0\) for \(j<N\), and neither \(D_N(y)\)
nor \(D_N(z)\) vanishes. This proves the nonvanishing assertion.
\(\square\)

The two ends have simple checks in the original source:
\[
 \mathcal C_N(X_0,y,z)=
       \frac{\kappa}{\sqrt N}
          \frac{D_N(y)D_N(z)}{(1+qy)(1+qz)},\qquad
 \mathcal C_N(X_d,y,z)=
       \kappa\sqrt N\,\frac{1-(yz)^N}{1-yz}.
 \tag{11}
\]
The second follows from \((Q;Q)_d=N\) and the complete cyclic
products in (7). It is regular when \(yz=1\) by its finite
geometric-sum interpretation, although that point is outside
\(\mathbb D^2\). These are the marked and unit end slices;
the intervening products retain all original boundary directions.

The last wall step must not be made homogeneous. Extending the
product in (7) formally to \(j=N\) would insert
\((Q;Q)_N=0\), although \(X_N=X_0\) and (9) is nonzero.
The nonzero forcing at the step \(X_d\longmapsto X_0\)
is exactly what restores the original slice. Thus a periodic
interpolation of the factorial weights cannot silently erase this
missing cyclic arrow.

## 3. A canonical derivative-free Cauchy period

For \(x,y,z\in\mathbb D\), put
\[
 \widehat{\mathcal C}_N=
       \frac{\mathcal C_N}{D_N(x)D_N(y)D_N(z)} .
 \tag{12}
\]
The exact finite representation is
\[
 \boxed{\quad
 \widehat{\mathcal C}_N(x,y,z)=
 \frac{\kappa}{N^{3/2}(1+qy)(1+qz)}
 \sum_{j=0}^{N-1}
 \frac{(Q;Q)_j(Qyz;Q)_j}
      {(-q^3y;Q)_j(-q^3z;Q)_j}
          \frac1{1+q^{-1}Q^{-j}x}.
 \quad}
 \tag{13}
\]
For a proof, \(\mathcal C_N(x,y,z)\) has degree below \(N\)
in \(x\). Consequently its quotient by \(D_N(x)\) is proper
rational with simple poles at \(X_j\). Since
\(D_N'(X_j)=-N/X_j\), its partial fractions are
\[
 \widehat{\mathcal C}_N(x,y,z)=
       \sum_{j=0}^{N-1}
       \frac{\mathcal C_N(X_j,y,z)}
                 {N D_N(y)D_N(z)}\,\frac1{1-x/X_j}.
 \tag{14}
\]
Insert (7) and separate the first factor in each denominator
to get (13).

Thus the wall residues and the complete finite Cauchy period
are prescribed, rather than fitted to an unknown source.
Every pole in (13) has nonzero residue when \(y,z\in\mathbb D\).
The full polynomial \(\mathcal C_N\) is regular at these points;
one must use (7), not evaluate (12) without canceling its norm
factor. Multiplication by all three \(D_N\)'s recovers the
original source inside the disk. No derivative, scalar phase,
or first Casimir normal has been omitted in passing from (3)
to this representation.

## 4. A uniform complex packet on the bulk wall

Use the initialized action
\[
 \Psi(x,y,z)=-\frac{\pi}{12}
 +\frac1{2\pi}\left[
  \operatorname{Li}_2(-x)+\operatorname{Li}_2(-y)
   +\operatorname{Li}_2(-z)+\operatorname{Li}_2(-xyz)
   -\operatorname{Li}_2(xy)-\operatorname{Li}_2(xz)
   -\operatorname{Li}_2(yz)\right]
 \tag{15}
\]
and amplitude
\[
                    B(x,y,z)=
             [(1-xy)(1-xz)(1-yz)]^{-1/2}.
 \tag{16}
\]
Both branches start from their power series in \(\mathbb D^3\).
At \(x=-e^{2\pi iu}\), \(0<u<1\), continue radially in \(x\).
The only unit-circle dilogarithm argument is \(e^{2\pi iu}\ne1\);
all other arguments lie strictly inside the disk. These boundary
values are locally analytic in \(u,y,z\), and
\[
 B(-e^{2\pi iu},y,z)=
 [(1+ye^{2\pi iu})(1+ze^{2\pi iu})(1-yz)]^{-1/2}
 \tag{17}
\]
is the branch equal to one at \(y=z=0\).

**Theorem 2.** Fix \(0<\delta<1/2\) and \(0<\rho<1\).
Uniformly for indices with
\[
          u_j=(j+1/2)/N\in[\delta,1-\delta],
                 \qquad |y|,|z|\le\rho,
\]
the actual original wall source obeys
\[
 \boxed{\quad
 \mathcal C_N(X_j,y,z)=
 \kappa e^{\,i\pi/4-\pi i/(8N)}
       D_N(y)D_N(z)\,B(X_j,y,z)
           e^{\,iN\Psi(X_j,y,z)}
                           (1+O_{\delta,\rho}(N^{-1})).
 \quad}
 \tag{18}
\]
The error is a complex value estimate, relative to the nonzero
displayed source. No real restriction on \(y,z\) is imposed.
It gives, in particular, uniform two-sided bounds for its modulus
by constant multiples of \(e^{-N\operatorname{Im}\Psi}\)
on these sets.

**Proof.** Write \(u=u_j\) and \(w=e^{2\pi iu}\).
Let \(s_j=\prod_{h=1}^j2\sin(\pi h/N)\).
The middle-calibrated sine-factorial estimate gives
\[
                         s_j=\sqrt N\,e^{NL(u)}
                                         (1+O_\delta(N^{-1})),
 \quad
 L(u)=\int_0^u\log(2\sin\pi v)\,dv,
 \tag{19}
\]
because \(j=Nu-1/2\). Its normalization follows from
\(s_js_{d-j}=N\) and trapezoidal Euler--Maclaurin between
the middle and a strict interior label, as proved in the prism
bridge. The exact phase of the complex factorial is
\[
 \begin{split}
 (Q;Q)_j
   &=(-i)^jq^{j(j+1)/2}s_j\\
   &=\sqrt N\,
      e^{\,i\pi/4-\pi i/(8N)}
      \exp\left\{N\left[L(u)+
                         \frac{i\pi}{2}(u^2-u)\right]\right\}
                                      (1+O_\delta(N^{-1})).
 \end{split}
 \tag{20}
\]

For \(|a|<1\), put
\[
 I_a(u)=\int_0^u\log(1-ae^{2\pi iv})\,dv
       =-\frac{\operatorname{Li}_2(ae^{2\pi iu})
                         -\operatorname{Li}_2(a)}{2\pi i}.
 \tag{21}
\]
The logarithms are anchored at \(a=0\). Their derivatives on
the real \(v\)-interval are bounded uniformly for \(a\) in a
closed interior disk. Ordinary Euler--Maclaurin, with the indicated
half-step offsets, gives
\[
 \begin{aligned}
 \log(Qyz;Q)_j
     &=NI_{yz}(u)-\tfrac12\log(1-yz)+O_{\delta,\rho}(N^{-1}),\\
 \log(-qy;Q)_{j+1}
     &=NI_{-y}(u)+\tfrac12\log(1+yw)
                                      +O_{\delta,\rho}(N^{-1}),
 \end{aligned}
 \tag{22}
\]
and the same formula for \(z\). The first sum samples
\(h/N\), \(1\le h\le j\); the second samples
\((h+1/2)/N\), \(0\le h\le j\). Expanding their upper
integration limit about \(u=(j+1/2)/N\) yields precisely
the endpoint half-weights in (22).

Substituting (20)--(22) in the exact product (7) gives amplitude
\[
                    [(1-yz)(1+yw)(1+zw)]^{-1/2}
                                      =B(-w,y,z)
 \tag{23}
\]
and exponent
\[
       L(u)+\frac{i\pi}{2}(u^2-u)
                         +I_{yz}(u)-I_{-y}(u)-I_{-z}(u).
 \tag{24}
\]
The unit-circle dilogarithm identities
\[
 \operatorname{Im}\operatorname{Li}_2(e^{2\pi iu})=-2\pi L(u),
 \qquad
 \operatorname{Re}\operatorname{Li}_2(e^{2\pi iu})
                         =\pi^2(u^2-u+\tfrac16)
 \tag{25}
\]
turn (24), using (21), exactly into \(i\Psi(-w,y,z)\).
The powers \(\sqrt N\) in (7) and (20) cancel. This proves
(18), with its full scalar phase. All error bounds are uniform
for the stated complex \(y,z\), since every regular factor in
(22) stays away from zero. \(\square\)

## 5. What the wall data do and do not control

Equation (13) is an exact, initialized Cauchy representation of the
whole universal tensor. Equation (18) gives a known nonzero
geometric principal amplitude on every strict bulk wall slice,
even for arbitrary compact complex values of the other two legs.
The result is not obtained by assigning a saddle coefficient.

It does not justify inserting only (18) term by term in (13) and
then discarding cancellation among its \(N\) terms. The two endpoint
layers \(j\) near zero or \(d\) are outside the stated uniform
wall asymptotic. A contour interpolation of the factorial weights
must retain their finite initialization and the forced last arrow
described after (11). An unchecked periodic quantum-gamma
interpolation could change the source.

In particular no estimate here transports the growing packet along
an arbitrary interior radial path. Nor does it move the assembled
Conway coefficient cycle or prove a lower bound after general
short fillings. Those questions require estimates for the complete
Cauchy period and the original global gluing.

## Complete proof sources and coverage

Both complete proof sources were read at the matching pins:

| Source | SHA-256 |
|---|---|
| [Forced original Rogers connection](research_centered_tensor_forced_rogers_connection.md) | 0d2ed84d814c892754f87dcda16d50167dc50acb845538720aa9e6abb9e3d8d7 |
| [Prism boundary and radial bridge](research_centered_tensor_prism_radial_bridge.md) | 892dfc5ef5e0774d45ccc44bc4f5122e7137d6185fe9191997e1b43d79003776 |

The first supplies the exact physical connection with its nonzero
forcing. The second supplies the initialized action and the
middle-calibrated sine-factorial estimate. The wall initializer,
residue products, Cauchy representation and uniform complex
two-leg wall packet are proved above. No novelty is claimed for
partial fractions or Euler--Maclaurin summation.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git
operation or earlier-final edit was performed.
