# The actual geometric cosine response near half frequency

Private exact-source theorem, 9 November 2026. A fixed sufficiently
small frequency interval below one half follows the selected inner
geometric branch in the original quantum observation. An exact
full-grid parity fold removes a spurious half-line endpoint. The
complete inner packet is retained as an exact bounded holomorphic
amplitude, after which a finite sampling contour separates the
principal charged integral from exponentially smaller aliases and
cutoff terms.

The result gives a uniform selected-action upper bound up to the
half-frequency endpoint. It also gives a nonzero Gaussian asymptotic
on every compact subinterval strictly below that endpoint. It is
local in frequency and does not establish an adequate bound for the
whole outgoing insertion or a short-filling theorem. No mathematical
numerical evaluation, saved-value arithmetic, or frozen-source edit
is used.

## 1. Original observation and the exact parity fold

Keep
\[
\begin{gathered}
 D=N-1,\quad q=e^{\pi i/N},\quad \eta=(-1)^D,\quad
 M=\lceil N/2\rceil,\quad U=\lfloor N/2\rfloor-1,\\
 c_j=2\cos((2j+1)\pi/N),\qquad
 u_j=\pi-(2j+1)\pi/N,\qquad c_j=-2\cos u_j,\\
 C_{N,3}=q^{3D^2/4},\qquad
 Q_N(u)=\mathcal K_{3,N}(-2,-2\cos u)
          =P_{3,N}(0,u).
\end{gathered}
\tag{1}
\]
Here \(Q_N\) is the complete original inner kernel, with its full
Hermite trace, both full edges and its original cubic crossing. The
last equality uses [the full single-vertex theorem, (1)](research_all_nonzero_degree_two_fillings.md).
Define the angular cosine polynomial and its original observation by
\[
 C_k(X)=T_k(-X/2),\qquad
 \mathcal O_{N,k}
    =\phi_N[R^3e_M\mathcal K_{3,N}(-2,\cdot)C_k].
\tag{2}
\]
Thus \(C_k(c_j)=\cos(k u_j)\). For the convention
\(T_k(X/2)\), multiply the response by \((-1)^k\).
All outside scalars in the transfer remain separate from (2).

Put
\[
 a_N(u)=
 \begin{cases}
  \sin u,&N\text{ even},\\
  \displaystyle\frac{\sin u\sin(u/2)}{\cos^2(\pi/(2N))},
                                      &N\text{ odd},
 \end{cases}
 \qquad
 \chi_N=
 \begin{cases}i,&N\text{ even},\\-1,&N\text{ odd}.\end{cases}
\tag{3}
\]
Notice \(a_N(-u)=\eta a_N(u)\). For every integer
\(0\le k\le\lfloor N/2\rfloor\), set
\(\delta=1/2-k/N\). The exact full-grid identity is
\[
\boxed{\quad
 \mathcal O_{N,k}
   =\frac{\chi_N C_{N,3}}2
      \sum_{j=0}^{D}a_N(u_j)Q_N(u_j)
        \exp\!\left[N\left(\frac{3iu_j^2}{4\pi}
                                      -i\delta u_j\right)\right].
\quad}
\tag{4}
\]

To prove (4), the original [radical contraction, (16)](research_mixed_next_three_outer_casimir_observation.md)
has weights
\[
 b_{Uj}=(-1)^{U+j}a_N(u_j),\qquad 0\le j\le U.
\tag{5}
\]
The exact original crossing values are
\(R(c_j)^3=C_{N,3}e^{3iNu_j^2/(4\pi)}\), by
[the Gaussian crossing transport, (10)--(12)](research_current_free_aw_crossing_transport.md).
Also
\[
 (-1)^j=e^{i\pi D/2}e^{-iNu_j/2},\qquad
 e^{-iNu_j}=\eta,
\]
so
\[
 e^{-iNu_j/2}\cos(ku_j)
       =\tfrac12\{e^{-iN\delta u_j}+\eta e^{iN\delta u_j}\}.
\tag{6}
\]
Reflection pairs the positive double nodes with their negative
copies, using \(Q_N(-u)=Q_N(u)\), the even cubic Gaussian and
the parity of \(a_N\). At odd levels the additionally included
node \(u=0\) has \(a_N(0)=0\). Thus (6) becomes precisely
the full \(N\)-point sum in (4). Its scalar is
\((-1)^Ue^{i\pi D/2}C_{N,3}=\chi_N C_{N,3}\).
The factor \(1/2\) is from this exact reflection.

At even levels \(\delta=0\) means \(k=N/2\), and
\(\cos(Nu_j/2)=0\) at every original double node. Therefore
\[
                    \mathcal O_{N,N/2}=0\qquad(N\text{ even}).
\tag{7}
\]
No nonzero assertion below includes that endpoint. Neither (4) nor
its subsequent use declares the Gaussian interpolant globally
periodic.

## 2. The exact local amplitude and the selected charged phase

Let \(S(u)=S_3(0,u)\), with its original additive constant,
and let \(M_3=\Re S(0)\). The full single-vertex theorem gives
on a fixed complex disk about zero
\[
 Q_N(u)=C_{N,3}N^{-3/2}A(u)e^{NS(u)}(1+O(N^{-1})),
\tag{8}
\]
where \(A\) is holomorphic and nonzero, \(S\) is even, and
the normalized remainder is uniformly holomorphic. On a smaller
fixed disk, define the exact function
\[
 A_N(u)=C_{N,3}^{-1}N^{3/2}e^{-NS(u)}Q_N(u).
\tag{9}
\]
It is holomorphic, uniformly bounded with each fixed derivative
on smaller disks, and satisfies \(A_N=A+O(N^{-1})\) there.
In particular (9), rather than an approximate list of nodal values,
is used in the contour below. Every inner charge, endpoint current
and algebraic Gaussian error is already inside this exact function.

The original selected branch has
\[
 c_+=\frac{1+2i+\sqrt{5-4i}}4,\qquad
 S''(0)=-\frac{c_+}{2\pi},\qquad \Re c_+>0,
\tag{10}
\]
by [the endpoint-root theorem, Section 3](research_mixed_next_outer_symbol_endpoint_roots.md).
Define
\[
 \Psi_\delta(u)=S(u)+\frac{3iu^2}{4\pi}-i\delta u.
\tag{11}
\]
The unique local selected stationary point is
\[
 \Psi_\delta'(u_\delta)=0,\qquad
 u_\delta=\frac{2\pi}{3+ic_+}\delta+O(\delta^3),
 \qquad u_0=0.
\tag{12}
\]
It is holomorphic in \(\delta\), and for sufficiently small
positive real \(\delta\), \(\Im u_\delta<0\).
Write
\[
       \mathcal S(\delta)=\Psi_\delta(u_\delta),\qquad
       \Gamma(\delta)=\Re\mathcal S(\delta).
\tag{13}
\]

**Theorem 1.** There exist fixed \(\delta_0>0\), \(\gamma>0\)
and \(C\) such that, for all sufficiently large levels of both
parities and all integers \(k\) with
\(0\le\delta=1/2-k/N\le\delta_0\),
\[
                  |\mathcal O_{N,k}|
                      \le C N^{-1}e^{N\Gamma(\delta)}.
\tag{14}
\]
More precisely, the response is a single local charged integral
given in (24) below, with all other sampling aliases, cutoff
connectors and removed original nodes bounded by
\(C e^{N(\Gamma(\delta)-\gamma)}\). The constants are
independent of \(k,N\) in this stated range.

The interval is fixed but only asserted to be sufficiently small.
No numerical width or coverage of the whole frequency interval is
claimed.

## 3. Fixed contour choices and their strict gaps

We give explicit inequalities determining the choices, so no
level-dependent saddle or alias condition is hidden. Shrink the
source disk in (9) to a disk of radius \(R>0\) on which
\[
 \Re\Psi_0''(u)\le-2\kappa<0,\qquad
                         |\Psi_0''(u)|\le B
\tag{15}
\]
for fixed \(\kappa,B>0\). This is possible by (10), since the
added crossing Hessian is purely imaginary. Evenness gives
\(\Psi_0'(0)=0\). For real \(x,y\) with the relevant segments
inside the disk, vertical Taylor expansion gives
\[
 \Re\Psi_\delta(x+iy)
   \le M_3-\kappa x^2+B|x||y|+\tfrac B2y^2+\delta|y|.
\tag{16}
\]
In particular, completing the square in \(x\) yields a constant
\(C_0\) such that the right side is at most
\(M_3+C_0y^2+\delta|y|\).

Choose \(a>0\) with \(2a<R/2\). Choose a fixed sufficiently
small \(h>0\), and then sufficiently small \(\delta_0>0\), so
that \(\{|x|\le2a,|y|\le h\}\) lies in the disk and
\[
\begin{split}
 C_0h^2+\delta_0h&\le h/2,\\
 2Bah+Bh^2/2+\delta_0h&\le\kappa a^2/8,\\
 |\Re u_\delta|&<a/4,\qquad
       -h/2<\Im u_\delta\le0\quad(0\le\delta\le\delta_0).
\end{split}
\tag{17}
\]
The first two inequalities hold by first taking \(h\) small and
then \(\delta_0\) small; the last follows from (12).
All later restrictions only shrink \(\delta_0\).

The full single-vertex theorem also gives constants \(c_3>0,C,b\)
such that on the entire real period
\[
 |Q_N(u)|\le CN^b
                   e^{N\{M_3-c_3(1-\cos u)\}},\qquad |u|\le\pi.
\tag{18}
\]
Its source is the same complete kernel as (1); this does not use
an off-grid extension of a shortened physical row. The weights
\(a_N(u_j)\) are uniformly bounded on that period. Thus the part
of (4) with \(|u_j|\ge a/2\) has an absolute bound
\(CN^{b+1}e^{N(M_3-\beta)}\), where
\(\beta=c_3(1-\cos(a/2))>0\). The original crossing and cosine
carriers have unit modulus on those nodes.

## 4. Exact finite sampling and all aliases

Write the local grid as \(u=2\pi(\ell+\rho_N)/N\), where
\(\rho_N=1/2\) at even levels and \(\rho_N=0\) at odd levels.
Choose symmetric midpoint cuts \(\pm\ell_N\), where
\[
 \ell_N=\frac{2\pi}{N}
     \left(\left\lfloor\frac{Na}{2\pi}-\rho_N\right\rfloor
                                   +\rho_N+\frac12\right).
\tag{19}
\]
Then \(\ell_N\to a\), and for all large \(N\),
\(a/2\le\ell_N\le2a\). At either vertical cut,
\(\eta e^{-iN(\pm\ell_N)}=-1\).

Use the exact simple-pole sampling kernel
\[
                 H_N(u)=\frac1{1-\eta e^{-iNu}}.
\tag{20}
\]
Its residue at each original grid point is \(1/(iN)\).
For the positively oriented rectangle with vertices
\(\pm\ell_N\pm ih\), the residue theorem therefore gives,
for every holomorphic \(f\) on the rectangle,
\[
 \sum_{|u_j|<\ell_N} f(u_j)
                 =\frac{N}{2\pi}\oint H_N(u)f(u)\,du.
\tag{21}
\]
This is a finite local identity. It assumes no periodicity of
\(f\) or of the crossing Gaussian.

Apply (21) to
\(f(u)=a_N(u)A_N(u)e^{N\Psi_\delta(u)}\).
At odd levels the residue at zero is zero because the
parity amplitude vanishes there; it is not an omitted simple node.

On the bottom edge \(y=-h\),
\(H_N=1+O(e^{-Nh})\). On the top edge \(y=h\),
\(H_N=O(e^{-Nh})\). These estimates retain the whole rational
kernel and hence all sampling aliases. Equations (16)--(17) show
that the bottom correction and the entire top integral have rate
at most \(M_3-h/2\), before fixed polynomial factors.

On the midpoint verticals,
\[
                  |H_N(\pm\ell_N+iy)|
                     =\frac1{1+e^{Ny}}\le1.
\tag{22}
\]
By (16)--(17) and \(\ell_N\ge a/2\), the phase there has rate
at most \(M_3-\kappa a^2/8\). Thus both entire vertical currents
are paid, including the point where they cross the real axis.
All amplitudes and lengths are uniformly bounded.

The surviving bottom integral has no sampling kernel. Cauchy's
theorem moves it to the horizontal line through \(u_\delta\),
oriented from \(-\ell_N+i\Im u_\delta\) to
\(\ell_N+i\Im u_\delta\). Its two additional endpoint connectors
lie on the same paid verticals and have the same bound. Write this
horizontal segment as \(\gamma_{N,\delta}\).

Combining the exact fold (4), the full source (9), all four sides
of (21), these two connectors and the removed-node bound (18),
gives a fixed \(\gamma_0>0\) and finite \(b_0\) with
\[
 \mathcal O_{N,k}
   =\frac{\chi_N C_{N,3}^2}{4\pi\sqrt N}
       \int_{\gamma_{N,\delta}}
          a_N(u)A_N(u)e^{N\Psi_\delta(u)}\,du
        +O\!\left(N^{b_0}e^{N(M_3-\gamma_0)}\right).
\tag{23}
\]
Every scalar in front of the integral comes from (4),(9),(21).
The inner unit angular charge and all its original currents are
retained through the full packet input; no wide-corridor theorem
with a different charge has been used.

Since \(\Gamma(\delta)=M_3+O(\delta^2)\), shrink
\(\delta_0\) so that \(\Gamma(\delta)\ge M_3-\gamma_0/2\).
Absorb the fixed polynomial into part of the remaining gap. For
some fixed \(\gamma>0\), (23) becomes
\[
\boxed{\quad
 \mathcal O_{N,k}
   =\frac{\chi_N C_{N,3}^2}{4\pi\sqrt N}
       \int_{\gamma_{N,\delta}}
          a_N(u)A_N(u)e^{N\Psi_\delta(u)}\,du
       +O\!\left(e^{N(\Gamma(\delta)-\gamma)}\right).
\quad}
\tag{24}
\]

Along the surviving horizontal line, (15) and stationarity give
\[
 \Re\Psi_\delta(u_\delta+x)
             \le\Gamma(\delta)-\kappa x^2
\tag{25}
\]
for the real offsets on that segment. The amplitudes are bounded,
so its absolute integral is at most
\(CN^{-1/2}e^{N\Gamma(\delta)}\). Substitution into (24)
proves (14), including \(\delta=0\). No algebraic error from
(8) has been summed separately in this argument.

## 5. Nonzero response away from the half-frequency endpoint

Fix any \(0<\delta_1\le\delta_0\). For integer sequences with
\(\delta\in[\delta_1,\delta_0]\), the same exact contour gives
\[
\boxed{\quad
 \mathcal O_{N,k}
   =\frac{\chi_N C_{N,3}^2}{2\sqrt{2\pi}}\,
       N^{-1}\,
       \frac{a^{\rm par}(u_\delta)A(u_\delta)}
                      {\sqrt{-\Psi_\delta''(u_\delta)}}
       e^{N\mathcal S(\delta)}(1+O(N^{-1})),
\quad}
\tag{26}
\]
where
\[
 a^{\rm par}(u)=
  \begin{cases}\sin u,&N\text{ even},\\
                \sin u\sin(u/2),&N\text{ odd}.
  \end{cases}
\tag{27}
\]
The square root in (26) has positive real part; this is defined
throughout the small interval by (15). Formula (26) is uniform on
the specified compact subinterval, separately at both parities.

For completeness, (25) makes the portions a fixed distance from
the saddle exponentially smaller. In a fixed saddle neighborhood,
the usual Taylor expansion on the real horizontal coordinate has
uniformly bounded analytic derivatives and strictly negative real
quadratic term. Integration of its Gaussian gives
\(\sqrt{2\pi/N}/\sqrt{-\Psi_\delta''(u_\delta)}\), with
relative error \(O(N^{-1})\). Here the exact amplitude obeys
\(A_N=A+O(N^{-1})\) with the corresponding derivative bounds,
and the odd factor \(\cos^{-2}(\pi/(2N))=1+O(N^{-2})\).
These replacements are made only in this single surviving
Gaussian integral, after (24), not in the oscillatory finite sum.

The original \(A\) is nonzero. For a sufficiently small
\(\delta_0\), (12) has \(u_\delta\ne0\) for every positive
\(\delta\), and neither sine in (27) vanishes. Thus the coefficient
in (26) is nonzero and uniformly bounded away from zero on each
fixed \([\delta_1,\delta_0]\). No such nonzero uniform statement
is asserted as \(\delta\to0\); (7) is retained exactly.

## 6. The oriented geometric action loss and its limitation

Stationarity in (12) gives
\[
 \Gamma'(\delta)=\Re(-iu_\delta)=\Im u_\delta<0
                          \quad(0<\delta\le\delta_0).
\tag{28}
\]
The adopted [oriented-root theorem](research_mixed_next_outer_oriented_root_barriers.md)
identifies this exact charged root with the unique root of
\(\mathscr F_+\) approaching the unit circle from outside.
After decreasing \(\delta_0\) if necessary, all its other outer
roots remain farther away. Therefore
\[
 -\Im u_\delta=r_+^{\rm out}(1/2-\delta),\qquad
 \Gamma(\delta)=M_3-
       \int_0^\delta r_+^{\rm out}(1/2-s)\,ds.
\tag{29}
\]
Writing \(c_+=A_c+iB_c\), this yields
\[
 M_3-\Gamma(\delta)
    =\frac{\gamma_{\rm g}}2\delta^2+O(\delta^4),\qquad
 \gamma_{\rm g}=
       \frac{2\pi A_c}{(3-B_c)^2+A_c^2}
                         >\frac{4\pi}{37}.
\tag{30}
\]
The full-symbol nearest-root integral instead has leading term
\(2\pi\delta^2/37\). Thus, on this fixed sufficiently small
interval, (14) is a source-specific quantum coefficient bound
following the selected oriented branch beyond that generic barrier.
It was obtained from the original exact observation; no factor of
the finite operator was dropped.

Extending this frequency interval far enough and combining the
coefficient response with the actual outgoing action profile remain
separate tasks. Neither (14) nor (26) supplies the required bound
for the whole remaining signed transfer, a finite list of exceptional
fillings, or a uniform macroscopic oriented inverse.

## 7. The same local source theorem for every fixed nonzero inner power

The finite fold and contour argument are not specific to the two
cubic powers. To state their precise generality, fix any integer
\(n\ne0\) and any integer \(m\), and retain the full original
inner source \(Q_{n,N}(u)=P_{n,N}(0,u)\). Write
\(\widehat Q_{n,N}(X)\) for its original canonical spectral
polynomial, so \(\widehat Q_{n,N}(-2\cos u)=Q_{n,N}(u)\).
Use the exact scalar
\(\epsilon_{n,N}\), phase \(S_n\) and amplitude \(A_n\)
of the full single-vertex theorem. In particular its phase/scalar
conventions for \(n=\pm1,\pm2\) are not replaced by the cubic
convention. Set
\[
\begin{split}
 \mathcal O_{n,m,N,k}
    &=\phi_N[R^m e_M\widehat Q_{n,N}C_k],\\
 C_{N,m}&=\exp\!\left(\frac{\pi i mD^2}{4N}\right),\\
 \Psi^{n,m}_\delta(u)
    &=S_n(0,u)+\frac{im u^2}{4\pi}-i\delta u,\\
 d_{n,m}&=\partial_u^2S_n(0,0)+\frac{im}{2\pi}.
\end{split}
\tag{31}
\]
The theorem's negative real Hessian gives \(\Re d_{n,m}<0\).
Thus there is a unique local charged saddle
\[
 u^{n,m}_\delta=\frac{i\delta}{d_{n,m}}+O(\delta^3),\qquad
 \Im u^{n,m}_\delta<0\quad(\delta>0\text{ small}),
\tag{32}
\]
and a charged action \(\mathcal S_{n,m}(\delta)
=\Psi^{n,m}_\delta(u^{n,m}_\delta)\).

**Corollary 2.** For every fixed pair \((n,m)\) as above, a fixed
sufficiently small \(\delta_0(n,m)>0\) has the conclusions
(14),(24),(26), with the corresponding phases and amplitudes and
with \(\chi_N C_{N,3}^2\) replaced throughout by
\(\chi_N C_{N,m}\epsilon_{n,N}\). In particular
\[
 |\mathcal O_{n,m,N,k}|
       \le C_{n,m}N^{-1}
              e^{N\Re\mathcal S_{n,m}(\delta)},
\qquad
 M_n-\Re\mathcal S_{n,m}(\delta)
       =-\frac12\Re(d_{n,m}^{-1})\delta^2+O(\delta^4).
\tag{33}
\]
The quadratic coefficient in the loss is strictly positive.
The nonzero asymptotic is restricted, as before, to fixed compact
subintervals \(0<\delta_1\le\delta\le\delta_0(n,m)\).

*Proof.* The radical weight (5) is independent of the crossing
power. Its original Gaussian value is
\(R(c_j)^m=C_{N,m}e^{imNu_j^2/(4\pi)}\) for every signed
integer \(m\). Therefore the exact parity fold (4) holds with
that Gaussian and \(Q_{n,N}\), without any change depending on
the parity of \(m\). The full single-vertex theorem supplies
both the bounded exact local amplitude
\(\epsilon_{n,N}^{-1}N^{3/2}e^{-NS_n(0,u)}Q_{n,N}(u)\)
and the strict whole-real-period tail. The real part of the new
Hessian is still negative, since the outer crossing adds only an
imaginary term. All choices in (15)--(17), the finite sampling
identity, its full rational alias estimates, and the surviving
Gaussian argument therefore apply for this fixed pair. Expansion
at (32) gives
\(\mathcal S_{n,m}(\delta)=S_n(0,0)
 +\delta^2/(2d_{n,m})+O(\delta^4)\), proving (33).
\(\square\)

No uniform interval over unbounded powers is asserted. The oriented
degree-eleven identification (29) is specific to \(n=m=3\); the
general corollary makes no unproved identification of other charged
branches with a polynomial factor. This local generality does not
establish stability under arbitrary fixed short partial fillings.
