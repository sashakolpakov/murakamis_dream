# Actual cyclic crossings: a sharp wrap gap and a Gaussian Morse adapter

24 November 2026. Research proof. Earlier finals and manuscripts are unchanged.

The actual complete-color E-cyclic crossing differs from the original
nilpotent crossing by a one-wrap matrix. Its sharp physical norm exponent
is the regular ideal tetrahedron volume divided by \(\pi\), strictly
smaller than the full crossing's Gaussian exponent. Consequently the
existing whole physical Gaussian model approximates the actual cyclic
crossing to every fixed algebraic order.

Projecting this model onto the complete actual pair intertwiner space
makes its error an exact intertwiner. The opposite-source Morse Gram
then bounds that error, after any spectator embedding, by its pair
physical Hilbert--Schmidt norm. No Gram condition number or spectator
dimension factor occurs. This is an absolute approximation at the
full crossing norm scale, not a geometric scalar lower bound.

## 1. Actual changing-source matrices and physical conventions

Fix \(N\ge2\), and put
\[
 d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad x=-q^{-1},\quad
 \gamma=x^N=(-1)^{N+1},\quad \kappa=q^{d^2/2},
\]
\[
 F_j=(Q;Q)_j,\qquad
 s_j=|F_j|=\prod_{h=1}^j2\sin(\pi h/N),\qquad F_0=s_0=1.
 \tag{1}
\]
All pair matrices use the original balanced orthonormal physical
basis \(w_a\otimes w_b\). Let \(E_\mu,F,K\) be [M, (2)]:
\[
 E_\mu w_a=(Q^{-a}-1)w_{a-1}\ (a>0),\quad E_\mu w_0=\mu w_d,
 \quad Fw_a=(1-Q^{a+1})w_{a+1},\quad Kw_a=xQ^{-a}w_a .
 \tag{2}
\]
Missing end arrows are zero. Take
\(|\mu_1|=|\mu_2|=1/N\).

Write \(R^\sigma_{\boldsymbol\mu}\) for the genuine checked
crossing of [B], with its complete Cartan scalar retained.
For either sign its input pair \(\boldsymbol\mu=(\mu_1,\mu_2)\)
has output source
\[
                  \boldsymbol\mu'
                         =(\gamma\mu_2,\gamma\mu_1).
 \tag{3}
\]
The two signs are inverses with the appropriate intermediate fibers.
They are not obtained by leaving the nilpotent matrix unchanged.
Let \(R^\sigma_0\) be the original nilpotent crossing, in the
same metric and normalization, and define
\[
                    \Delta^\sigma_{\boldsymbol\mu}
                           =R^\sigma_{\boldsymbol\mu}-R^\sigma_0 .
 \tag{4}
\]
No deformation of the meridian or of the quantum root is used.

## 2. The exact one-wrap entries, including the negative sign

The checked positive matrix is \(\kappa\mathsf S D\) times the
finite Euler sum [B, (7)]
\[
 \sum_{k=0}^{d}
       \frac{(-1)^kq^{k^2}}{F_k}\,E_{\mu_1}^k\otimes F^k ,
 \tag{5}
\]
where \(\mathsf S\) flips the heads and \(D\) is the original
unitary Cartan diagonal at complete color.
For input \((a,b)\), a nonzero term requires \(b+k\le d\).
If \(k\le a\), it is precisely the nilpotent entry.
If \(a<k\), it wraps once, has output \((b+k,r)\) with
\(r=a-k+N\), and belongs to \(\Delta^+_{\boldsymbol\mu}\).
There is at most one term at any specified input and output.

Since \(s_d=N\) and \(|\mu_1|=1/N\), the wrapped lowering product
has modulus \(s_a/s_r\). Therefore the exact wrapped entry obeys
\[
 \left|(\Delta^+_{\boldsymbol\mu})_{(b+k,a-k+N);(a,b)}\right|
 =\frac{s_a s_{b+k}}{s_{a-k+N}s_b s_k}
 =\frac{s_a s_{b+k}s_{k-a-1}}{N s_b s_k},
 \quad 0\le a<k\le d-b .
 \tag{6}
\]
The last equality is the exact reflection identity
\(s_j s_{d-j}=N\); in particular its index is \(k-a-1\).
All other entries of this difference are zero.
Every such entry raises total integer degree by \(N\).

For the actual negative crossing first flip the input, apply \(D^{-1}\),
and then use the inverse Euler coefficients \(q^k/F_k\), in the
recovered positive-source fiber, as prescribed in [B, Section 4].
The recovered donor source still has modulus \(1/N\).
Its wrapped terms have donor \(b\), recipient \(a\), \(b<k\le d-a\),
and output \((b-k+N,a+k)\). Consequently
\[
 \left|(\Delta^-_{\boldsymbol\mu})_{(b-k+N,a+k);(a,b)}\right|
 =\frac{s_b s_{a+k}}{s_{b-k+N}s_a s_k}.
 \tag{7}
\]
The inverse Euler coefficients have the same moduli as those in (5);
the preceding Cartan and flip are unitary. This proves (7) directly,
without asserting a conjugation identity for the full cyclic matrices.
Both signs thus have the same set of wrapped entry magnitudes.
The external phases and source phases remain in the actual matrices.

## 3. Sharp physical norm exponent on the entire wrapped support

Let
\[
 h(u)=\int_0^u\log(2\sin\pi v)\,dv,\quad
 \Lambda(\theta)=-\int_0^\theta\log(2\sin v)\,dv,\quad
 v_3=3\Lambda(\pi/3).
 \tag{8}
\]
The endpoint-uniform sine-product estimate in [G] is
\(\log s_j=Nh(j/N)+O(\log N)\) for every \(0\le j<N\).
Apply it to the first expression in (6). With
\((u,v,t)=(a,b,k)/N\), its logarithm is
\[
 NS_{\rm w}(u,v,t)+O(\log N),\qquad
 S_{\rm w}=h(u)+h(v+t)+h(t-u)-h(v)-h(t),
\]
\[
                 0\le u\le t,\qquad 0\le v\le1-t.
 \tag{9}
\]
Here \(h(1+u-t)=-h(t-u)\) was used. The actual grid has \(a<k\)
and \(b+k\le N-1\); using its compact closure is valid for the
upper bound. All boundary factorial lengths are included.

For \(0<t<1\), the function \(h(u)+h(t-u)\) is strictly convex:
\[
 \frac{d^2}{du^2}\{h(u)+h(t-u)\}
       =\frac{\pi\sin\pi t}{\sin\pi u\,\sin\pi(t-u)}>0 .
 \tag{10}
\]
It therefore has maximum \(h(t)\) at the two endpoints.
The recipient interval \(h(v+t)-h(v)\) is strictly concave,
with unique maximum at \(v=(1-t)/2\) and value
\(-2h((1-t)/2)\). Thus
\[
 \max S_{\rm w}
       =\max_{0\le t\le1}-2h((1-t)/2)
       =-2h(1/6)=:M_{\rm w}=v_3/\pi .
 \tag{11}
\]
The last maximum has \(t=2/3\).
Both closure points \(u=0,t\) attain it, with \(v=1/6\);
no uniqueness of the full boundary maximizer is asserted.
To obtain the value, \(h'\) changes sign at \(1/6\) on \([0,1/2]\).
The identity
\(h(t)=2h(t/2)-2h((1-t)/2)\), proved by differentiation,
gives \(3h(1/3)=2h(1/6)\), hence the last equality in (11).
Continuity includes \(t=0,1\).

There are at most \(N^3\) wrapped entries. This proves the
upper Hilbert--Schmidt and operator bounds with logarithmic error.
For the lower bound take \(a=0\), \(k\) nearest \(2N/3\), and
\(b\) nearest \(N/6\), chosen within \(b+k\le d\).
For all sufficiently large \(N\) this is admissible, and its exact
modulus is \(s_{b+k}s_{k-1}/(N s_b s_k)\).
The same uniform factorial estimate gives its logarithm
\(NM_{\rm w}+O(\log N)\). A matrix norm dominates an entry.
Equation (7) proves the same bounds for the negative sign.
We have therefore proved, uniformly in the source phases,
\[
 \boxed{\quad
 \log\|\Delta^\sigma_{\boldsymbol\mu}\|_{\rm op}
 =\log\|\Delta^\sigma_{\boldsymbol\mu}\|_{\rm HS}
 =NM_{\rm w}+O(\log N).
 \quad}                                                     \tag{12}
\]
The equalities in (12) are asymptotic statements, not equality of norms.

## 4. A whole Gaussian in the updated cyclic fibers

Let \(\mathfrak G^\sigma_{N,J}\) be the untilted whole physical
Gaussian model of [G, (10)], at a fixed order \(J\ge0\).
It keeps the original unwrapped entry phase and support.
That theorem proves
\[
 \|R^\sigma_0-\mathfrak G^\sigma_{N,J}\|_{\rm HS}
     \le C_JN^{-(J+1)/2}\|R^\sigma_0\|_{\rm HS},\qquad
 \|R^\sigma_0\|_{\rm HS}
      =\tfrac12 N^{1/4}e^{NM_0}(1+O(N^{-1})),
 \quad M_0=2G_{\rm Cat}/\pi .
 \tag{13}
\]
Here \(G_{\rm Cat}=\sum_{r\ge0}(-1)^r/(2r+1)^2\).
There is a strict exponent gap \(M_0>M_{\rm w}\), without
needing a numerical comparison. Indeed [G]'s reduced unwrapped
action at Euler length \(t=2/3\) is
\[
 -4h(1/6)-h(2/3)
       =-\tfrac{10}{3}h(1/6)=\tfrac53 M_{\rm w}>M_{\rm w}.
 \tag{14}
\]
Since \(M_0\) is its maximum, this proves the gap.
The polynomial factors in (12) are consequently absorbed by
every fixed power of \(N^{-1}\) relative to (13). The triangle
inequality gives
\[
 \|R^\sigma_{\boldsymbol\mu}-\mathfrak G^\sigma_{N,J}\|_{\rm HS}
       \le C'_JN^{-(J+1)/2}\|R^\sigma_0\|_{\rm HS}
 \tag{15}
\]
for all sufficiently large integer levels, with no parity restriction.
The constants are uniform in \(|\mu_1|=|\mu_2|=1/N\).

Define the complete physical intertwiner space by full matrix equations:
\[
 \mathcal I^\sigma_{\boldsymbol\mu}
 =\{A:\ A E_{\rm in}=E_{\rm out}A,\ 
          A F_{\rm in}=F_{\rm out}A,\ 
          A K_{\rm in}=K_{\rm out}A\}.
 \tag{16}
\]
The total pair generators use (2), its actual coproduct, and the
input/output sources (3). Let \(\Pi^\sigma_{\boldsymbol\mu}\)
be the physical Hilbert--Schmidt orthogonal projection onto (16), and set
\[
       \widehat R^\sigma_{\boldsymbol\mu,N,J}
             =\Pi^\sigma_{\boldsymbol\mu}\mathfrak G^\sigma_{N,J},
       \qquad
       \mathcal E^\sigma_{\boldsymbol\mu,N,J}
             =R^\sigma_{\boldsymbol\mu}
                         -\widehat R^\sigma_{\boldsymbol\mu,N,J}.
 \tag{17}
\]
This is a specified finite projection, determined by the displayed
head matrices, not by an unknown knot scalar.
The space (16) is closed and contains the actual \(R^\sigma_{\boldsymbol\mu}\).
Orthogonal projection therefore proves
\[
 \mathcal E^\sigma_{\boldsymbol\mu,N,J}\in
                      \mathcal I^\sigma_{\boldsymbol\mu},\qquad
 \|\mathcal E^\sigma_{\boldsymbol\mu,N,J}\|_{\rm HS}
       \le C'_JN^{-(J+1)/2}\|R^\sigma_0\|_{\rm HS}.
 \tag{18}
\]
All physical matrix coordinates and all intertwining constraints
are used. No intermediate Casimir is replaced by nodal eigenvalues.
No constant dimension or smooth variation of (16) is required.
The projection need not preserve the Gaussian's entrywise phase
description, and no cost bound for explicitly computing it is asserted.

## 5. Spectator-free error in the source-compatible Morse Gram

Embed the error (17) on its actual neighboring pair in any
opposite-source odd-width slice of [M], using identities on spectators.
Use its correctly updated output labels. Pair \(E,F,K\)
intertwining implies intertwining of the full iterated coproduct:
the earlier terms contain the pair \(K\), the local terms its \(E\),
and the later terms pass unchanged. In particular
\(T_{\rm out}\mathcal E=\mathcal E T_{\rm in}\)
for the common normalization of [M, (15)].

Apply the exact averaging inequality [M, (18)] to this embedded map.
Its physical operator norm is the pair operator norm, which is
bounded by the pair Hilbert--Schmidt norm in (18). Hence
\[
 \boxed{\quad
 \|\mathcal E^\sigma_{\boldsymbol\mu,N,J}\otimes I_{\rm spec}
                         \|_{J_{\rm out}\leftarrow J_{\rm in}}
 \le C'_JN^{-(J+1)/2}\|R^\sigma_0\|_{\rm HS}
 \le C''_J N^{1/4-(J+1)/2}e^{NM_0}.
 \quad}                                                     \tag{19}
\]
No condition number of \(J_{\rm in}\) or \(J_{\rm out}\) is used.
There is no spectator Hilbert--Schmidt dimension factor.
In particular (19) is valid at an opposite-center pair whose total
pair \(E^N\) is zero: the averaging is on the odd whole slice,
not on a nonexistent cyclic pair normalization.

The corrected models and the literal cups/caps of [M] can be composed
as intertwiners in the fixed original Morse presentation.
Their errors remain absolute estimates at the scale in (19).
The two corrected signs are not asserted mutual inverses or a new
braiding, and their products are not asserted equal to the original word.
Every original cap, marked closing, framing and external scalar remains.
The error may exceed the actual geometric packet or closing overlap;
no nonzero cap projection or scalar geometric lower follows.

## Complete inputs and closest coverage

[G, Section 4] already projects its nilpotent Gaussian onto the full
physical algebra. [P, Section 4] already uses physical \(E,F,K\)
projection and warns that it changes a phase representation.
[C] already controls a different positive-degree Euler completion
and can damp its carry exponentially without changing the source.
No novelty is claimed for orthogonal projection or finite-group averaging.
The addition is (6)--(12) for the actual semicyclic wraps, followed by
the updated-fiber Gaussian estimate and the no-condition-number,
spectator-free Morse estimate (19). It supplies no off-root normal
continuation, geometric relative error, or finite-exception theorem.

All five complete matching texts were read. Only written mathematics
and text/hash operations were used. No earlier final was edited.

| Label | Complete text | SHA-256 |
| --- | --- | --- |
| B, source, 247 lines | [Actual changing-source crossings](balanced_verma_coherent_braiding.md) | 0203bdd7dbb36a4f8deb1c310b3445608e53d10922049447da8eecec4f87d1c4 |
| G, source, 306 lines | [Whole physical Gaussian](research_full_physical_crossing_gaussian_packet.md) | 7f1b9932f88aa549bc55088b6f056f5a362548bc51c9fdd7c6b00469e725f531 |
| M, source, 341 lines | [Source-compatible Morse Gram](research_opposite_source_morse_gram.md) | d676b2624a75c929027150aad0cdb33fa6d720643e97e86a8c5bb43c9dc951c9 |
| C, coverage, 259 lines | [Tame positive-degree carry](actual_exponentially_tame_carry_completion.md) | b109effeff1f963669867440a6f1cb314f0ac55e4ccadbd71e20bd9acea4245d |
| P, coverage, 285 lines | [Complete physical intertwiner projection](actual_projected_transfer_word_and_remaining_seams.md) | ba5e693ffc5e66b1a3f0ff8973a54a5d96436308dc718125a5504cf802d9c384 |
